//forward decls
struct server;
struct client;

struct world;
struct environment;

struct video;
struct sound;

struct character;
struct stats;

struct player;
struct pokedex;

struct pokemon;

struct sprite;
struct tile;
struct event;
struct item;
////////////////////////////////////////////////////////////////////////////////////////////////////
struct server {
  unsigned int  ipAddress : 32;
  unsigned short port     : 16;
  void start (void) throw (std::runtime_error);
  void stop  (void) throw (std::runtime_error);
  template<class data> void transmit (const data&) throw (std::runtime_error);
};

struct client {
  void connect (const unsigned int&, const unsigned int&) throw (std::runtime_errer);
  template<class data> data& recieve (void) const throw (std::runtime_error);
  // ^ this is to be used as a callback for the syncronous socket connection
};
/*-----------------------------------------*/
struct world : server {
  void tick (void) throw (std::runtime_error); //broadcasts tick signal over the connection
};

struct environment : client {
  struct video {
    std::string fileToDisplay;
	unsigned int x,y,z;
    virtual void display (void) throw (std::runtime_error);
	virtual vodid swipe   (void) throw (std::runtime_error);
  };

  struct sound {
    std::string fileToPlay
	virtual void play  (void) throw (std::runtime_error);
	virtual void stop  (void) throw (std::runtime_error);
	virtual void pause (void) throw (std::runtime_error);
  };

  //I intend that we will inherit from this, so that a tile has a singular image and sound associated to it
  struct tile : video, sound {} *map;
  
  struct event {} *state;
};
/*-----------------------------------------*/

struct character : client {
  struct stats {};
  struct item {};
  struct sprite : typename environment::video, typename environment::sound {};
};
/*-----------------------------------------*/
struct player : character {
  bool npc;
  struct pokedex : typename character::stats {};
};

struct pokemon : character {};