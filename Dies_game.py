import os
import random
import logging
import datetime


SPONSOR_NAME = os.environ.get("SPONSOR_NAME", "Default_Sponsor")
PLAYER_1_NAME = os.environ.get("PLAYER_1", "Player_1")
PLAYER_2_NAME = os.environ.get("PLAYER_2", "Player_2")

# ---------- Logging Setup ----------
WORKSPACE = r'D:\PythonProjects\Jenkins_Jobs\Dies_Game'
os.makedirs(WORKSPACE, exist_ok=True)
today_date = datetime.datetime.today().strftime('%Y-%m-%d')

log_file = os.path.join(WORKSPACE, f"{SPONSOR_NAME}_{today_date}.log")

logging.basicConfig(
    level=logging.INFO,
    filename=log_file,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Dice game Jenkins job started")

# ---------- Game Logic ----------
player_1 = 0
player_2 = 0
roll = 1
WIN_SCORE = 20

while player_1 < WIN_SCORE and player_2 < WIN_SCORE:

    p1_die = random.randint(1, 6)
    player_1 += p1_die
    logging.info(f"{PLAYER_1_NAME} | Roll {roll} | Die={p1_die} | Total={player_1}")

    if player_1 >= WIN_SCORE:
        break

    p2_die = random.randint(1, 6)
    player_2 += p2_die
    logging.info(f"{PLAYER_2_NAME} | Roll {roll} | Die={p2_die} | Total={player_2}")

    if player_2 >= WIN_SCORE:
        break

    roll += 1

# ---------- Result ----------
if player_1 > player_2:
    logging.info(f"Winner: {PLAYER_1_NAME}")
elif player_2 > player_1:
    logging.info(f"Winner: {PLAYER_2_NAME}")
else:
    logging.info("Match Draw")

logging.info("Dice game Jenkins job completed")
print("Dice game completed successfully")
