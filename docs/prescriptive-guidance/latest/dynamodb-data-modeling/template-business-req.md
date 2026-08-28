---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/template-business-req.html
---

# Business requirements assessment template
<a name="template-business-req"></a>

Provide a description for the use case:

|
|
| Description: Imagine that you are building an online multiplayer game. In your game, groups of 50 players join a session to play a game, which typically takes around 30 minutes to play. During the game, you have to update a specific player's record to indicate the amount of time the player has been playing, their statistics, or whether they won the game. Users want to see earlier games they've played, either to view the games' winners or to watch a replay of each game's action. |
| --- |

Provide information about your users:

|
|
| User | Description | Expected number |
| --- |--- |--- |
| *Game player* | *Online game player.* | *1 MM* |
| *Development team* | *Internal team that will use the game statistics to improve the*<br />*game experience.* | *100* |

Provide information about the sources of data and how data will be ingested:

|
|
| Source | Description | User |
| --- |--- |--- |
| *Online game* | *Game players will create profiles and start new games.* | *Game player* |
| *Game app* | *Game app will automatically collect statistics about the games, such as start and end time, number of players, position of each player, and map for the game.* |   |

Provide information about how data will be consumed:

|
|
| Consumer | Description | User |
| --- |--- |--- |
| *Online game* | *Game players will view profiles and review their game statistics.* | *Game player* |
| *Data analytics* | *The game development team will extract game statistics for data analysis and to improve the user experience. Data will be exported from the data store and imported into Amazon S3 to support analytics through a Spark application.* | *Development team* |

Provide a list of entities and how they are identified:

|
|
| Entity name | Description | Identifier |
| --- |--- |--- |
| *Game Player* | *Stores information such as identification, address, demographics, interests for each user (gamer).* | *Username* |
| *Game Instance* | *Provides information about each game played, including creator, start, end, and map Yplayed.* | *Game ID* |
| *Game User Mapping* | *Represents the many-to-many relationships between users and games.* | *Game ID AND Username* |

Create an ER model for the entities:

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/images/guide-img/225c2600-95f1-4c8c-9e23-419bc7ae3c55/images/362b697f-a9cc-47e7-9481-85d2f913d05e.jpeg)

Provide high-level statistics about the entities:

|
|
| Entity Name | Estimated \# of records | Record size | Notes |
| --- |--- |--- |--- |
| *Game Player* | *1 MM* | *< 1 KB* | *The game platform has about 1 MM users.* |
| *Game Instance* | *6 MM*<br />*(100,000K/day \* 60 days)* | *< 1 KB* | *On average, there are 100K games every day. We need to store the last 60 days.* |
| *Game User Mapping* | *300 MM*<br />*(6 MM games \* 50 players)* | *< 1 KB* | *On average, each game has 50 players that we need to store information about.* |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
