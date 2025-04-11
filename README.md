# CounterStrike 2 Bot AI

This project provides a collection of custom AI behavior trees for Counter-Strike 2. It supports various game modes such as Competitive, Deathmatch, and Wingman. Designed for both single-player and server use, it enhances bot gameplay with customizable and extensible behaviors.

---

## 📁 Project Structure

- `competitive/` – Behavior trees for Competitive matches  
- `wingman/` – Behavior trees for Wingman mode  
- `deathmatch/` – Behavior trees for Deathmatch  
- `cfg/` – Configuration files to load the AIs via console  
- `format-kv3-files.py` – Custom formatter for `.kv3` files  

---

## ⚙️ Setup

1. **Locate your CS2 installation folder**  
Usually found at:  
`C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike`

2. **Create the `ownscripts` folder**  
Inside:  
`Counter-Strike\game\csgo`  
Create a folder called:  
`ownscripts`

3. **Clone this repository into `ownscripts`**  
Open a terminal and run:
    ```bash
    git clone https://github.com/flovo543/CS2AI.git "C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike\game\csgo\ownscripts\CS2AI"
    ```

4. **Copy the config files**  
Copy the contents of the `cfg/` folder from this repo to:
    ```bash
    C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike\game\csgo\cfg
    ```

## 🎮 Usage In-Game

1. **Start CS2 and open the developer console (`~`)**

2. **Load the desired AI config using `exec`**:
   - **Competitive**:
     ```bash
     exec aicomp
     ```
   - **Wingman**:
     ```bash
     exec aiwing
     ```
   - **Deathmatch**:
     ```bash
     exec aideath
     ```

3. **On some servers, you have to run this first**:
   ```bash
   exec bot_config


## 🛠 Development

### KV3 Formatting

`.kv3` files are used to define AI behavior trees. To maintain consistency, use the provided formatter:

#### Custom Formatter Script

This repo includes a Python formatter for `.kv3` files (without it developing wont be fun):
```bash
format-kv3-files.py
```

#### VSCode Integration

To auto-format `.kv3` files in **VSCode** using a custom local formatter:

1. **Open the CS2AI folder as a project** in VSCode.

2. Install the **Custom Local Formatters** extension from the VSCode marketplace.
   
3. Open your `settings.json` and add the following:
   ```json
   "customLocalFormatters.formatters": [
     {
       "command": "python format-kv3-files.py",
       "languages": ["kv3"]
     }
   ]

4. Save the configuration and it will automatically format `.kv3` files when you save them.


### Adding Your Own AI

To create a new AI:

1. **Create a `.kv3` file**  
   Place it in a new folder
   Example: `competitive/bt_main.kv3`

2. **Create a corresponding `.cfg` file** in the `cfg/` folder
   Example: `cfg/aicomp`

3. **Set the AI path in the `.cfg` file**:
   ```bash
   mp_bot_ai_bt ownscripts/CS2AI/competitive/bt_main.kv3
    ```

4. **Load it in-game** using:
    ```bash
    exec aicomp
    ```

## ✅ Notes

- Make sure `developer console` is enabled in CS2 settings.
- You may need to call `exec aiflush` after adding new AI scripts.