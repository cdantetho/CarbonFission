# nuke_uwu
----------------------

## - nuke_uwu Description -
##### Multi-function Discord bot coded in Python
##### Current Version: v1.1.9
##### Contributors: 
 - Dante (Dante#3456)
 - Sreud (@𝕊 𝕣 𝕖 𝕦 𝕕#1950)

----------------------

## - nuke_uwu Commands -
*Command Prefix: &&*

### - 

####kick
Usage: kick @user
Description: Kicks specific member in guild. (Functional) 

####kickAll
Usage: kickAll
Description: Kicks all members in the guild. Will print statistics in console with number of users kicked and number of users that we failed to kick. (Functional) 

####ban
Usage: ban @user
Description: Bans specific member in guild. (Functional) 

####banAll
Usage: banAll
Description: Bans all members in the guild. Will print statistics in console with number of users banned and number of users that we failed to ban. (Functional) 

####rename
Usage: rename @user [NicknameToApply]
EXCEPTION: If [NicknameToApply] contains "reset", it will reset the user's nickname to their original username.
Description: Renames specific member in guild. Will print statistics in console about the user you renamed and what you renamed them. (Functional) 

####renameAll
Usage: renameAll [NicknameToApply]
EXCEPTION: If [NicknameToApply] contains "reset", it will reset all of the user's nickname's to their original username.
Description: Renames all members in the guild to a specified nickname. Will print statistics in console with number of users renamed and number of users that we failed to rename. (Functional) 

####dm
Usage: dm @user [MessageToSend]
Description: Private messages a specific message to a specific member in guild. (Functional) 

####dmAll
Usage: dmAll [MessageToSend]
Description: Private messages a specific message to all the members in guild. Will print statistics in console with number of users renamed and number of users that we failed to rename. (Functional) 

####spam
Usage: spam [AmountOfTimesToSendMessage] [MessageToSend]
Description: Spams a specific message X amount of times in the channel the command is called in. Will print statistics in console with information on the message spammed and amount of times spammed. (Functional) 

####rolespam
Usage: rolespam [AmountOfRolesToCreate] [RoleName]
Description: Spam creates roles with a specific name a specified amount of times. Will print statistics in console with information on the role spammed and amount of times spammed. (Functional) 

####channelspam
Usage: channelspam [AmountOfChannelsToCreate] [ChannelName]
Description: Spam creates text channels with a specific title a specified amount of times. Will print statistics in console with information on the text channel spammed and amount of times spammed. (Functional) 

####listAll
Usage: listAll [condition]
Available conditions
 - channels
 - roles
 - emojis
 - all (includes channels, roles, and emojis)
Description: Lists all items in the specified category. Will print statistics in console with information on the category, amount of items, and amount that failed to be retrieved. (Functional) 

####deleteAll
Usage: deleteAll [condition]
Available conditions
 - channels
 - roles
 - emojis
 - all (Channels, roles, and emojis)
Description: Deletes all of the specified server items. Will print statistics in console with information on the type of item, amount deleted, and amount that failed to be deleted. (Functional) 

####destroy
Usage: destroy
Description: Meant to be used to destroy a server. It will delete all emojis, channels, roles, then ban all users. (Functional - Untested) 