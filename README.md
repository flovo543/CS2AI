Section for setup: 
- Create folder called ownscripts in game/csgo in the counterstrike folder (often in Program(x86)/Steam/steamapps/common/Counter-Strike) and clone this project into it
- Copy the content of cfg folder to game/csgo/cfg

Section for use:
- Call on of the cfgs ingame (exec)
- Sometimes (on servers) you have to call bot_config first

Section for development:
- kv3 formatter (explain use of it)
- Short explanation: Create own kv3 file (Example: link to bt_main) + create cfg fild (Example: aicomp) - important here is to change the bot ai path: mp_bot_ai_bt ownscripts/CS2AI/competitive/bt_main.kv3;
