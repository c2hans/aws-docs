---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/template-access-patterns.html
---

# Access-patterns template
<a name="template-access-patterns"></a>

Collect and document information about the access patterns for the use case by using the following fields:

|
|
| Field | Description |
| --- |--- |
| **Access pattern** | Provide a name for the access pattern. |
| **Description** | Provide a more detailed description of the access pattern. |
| **Priority** | Define a priority for the access pattern (high, medium, or low). This defines the most relevant access patterns for the application. |
| **Read or write** | Is it a read access or write access pattern? |
| **Type** | Does the pattern access a single item, multiple items, or all items? |
| **Key attribute** | What is the key attribute used to access data? |
| **Filter** | Does the access pattern require any filter? |
| **Sort** | Does the result require any sorting? |

## Template
<a name="access-pattern-example"></a>

|
|
| Access pattern | Description | Priority | Read or write | Type (single item, multiple items, or all) | Key attribute |  Filters | Result ordering |
| --- |--- |--- |--- |--- |--- |--- |--- |
| *Create user profile* | *User creates a new profile.* | *High* |  *Write* | *Single item* | *Username* |  *N/A* |  *N/A* |
| *Update user profile* | *User updates their profile.* | *Medium* | *Write* | *Single item* | *Username* | *Username = current user* | *N/A* |
| *Get user profile* | *User reviews their profile.* | *High* | *Read* | *Single item* | *Username* | *Username = current user* | *N/A* |
| *Create a game* | *User creates a new game.* | *High* | *Write* | *Single item* | *GameID* | *N/A* | *N/A* |
| *Find open games* | *User searches for open games. Search results are  sorted by start timestamp in descending order.* | *High* | *Read* | *Multiple items* |   | *GameStatus = open* | *Start timestamp descendent* |
| *Find open games by map* | *User searches for open games by using a specific map sorted by start timestamp in descending*<br />*order.* | *Medium* | *Read* | *Multiple items* |   | *GameStatus = open and Map = XYZ* | *Start timestamp descendent* |
| *View game* | *User reviews the details of a game.* | *High* | *Read* | *Single item* | *GameID* | *N/A* | *N/A* |
| *View users in a game* | *User gets a list of all the users in a game.* | *Medium* | *Read* | *Multiple items* |   | *GameID = XYZ* | *N/A* |
| *Join user to a game* | *User joins an open game.* | *High* | *Write* | *Single item* | *GameID and Username* | *GameStatus = open* | *N/A* |
| *Start a game* | *User starts a new game.* | *High* | *Write* | *Single item* | *GameID* | *N/A* | *N/A* |
| *Update game for user* | *Update user position in the game.* | *Medium* | *Write* | *Single item* | *GameID and Username* | *N/A* | *N/A* |
| *Update game* | *Game ends; update statistics.* | *Medium* | *Write* | *Single item* | *GameID* | *N/A* | *N/A* |
| *Find all past games for a user* | *List all games that a user played ordered by the start timestamp of the game.* | *Low* | *Read* | *Multiple items* | *Username and GameID* | *Username = current user* | *Start timestamp* |
| *Export data for data analytics* | *Development team will run a batch job to export data to Amazon S3.* | *Low* | *Read* | *All* | *N/A* | *N/A* | *N/A* |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
