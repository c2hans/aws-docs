---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/working-with-data-apps.html
---

# Working with data in apps in Quick
<a name="working-with-data-apps"></a>

You can persist and manage data within your apps in Quick apps in multiple ways.

## Built-in app storage
<a name="apps-builtin-storage"></a>

The simplest way to persist data is with built-in app storage. It is a key-value system that requires no external setup and scales to support large numbers of records.

### Storage scopes
<a name="apps-storage-scopes"></a>
+ **Private storage** — Data visible only to the current user. Use for personal settings, preferences, saved filters, bookmarks, and per-user state.
+ **Shared storage** — Data visible to anyone with app access. Use for collaborative lists, comments, votes, shared configuration, and team data.

### Storage operations
<a name="apps-storage-operations"></a>

| Operation | Private | Shared | Description |
| --- | --- | --- | --- |
| Put Item | Yes | Yes | Store or update a key-value item. |
| Get Item | Yes | Yes | Retrieve an item by key. |
| List Items | Yes | Yes | List items with optional key prefix filter. |
| Delete Item | Yes | Yes | Remove an item by key. |
| List by Tag | No | Yes | Query shared items by tag (secondary index). |

### Key concepts
<a name="apps-storage-concepts"></a>
+ **Tables** — Logical groupings for your data. You define table names; no setup is required.
+ **Keys** — Each item has a unique key within its table. Keys can be up to 255 characters.
+ **Values** — String values up to 350 KB. Use JSON serialization for structured data.
+ **Tags (shared only)** — Optional categorization strings on shared items. Tags enable efficient querying by category.
+ **Write modes** — UPSERT (default) overwrites existing items. INSERT fails if the key already exists, which is useful for preventing duplicates.

**Note**
Each app has completely separate storage. Data persists across user sessions and app reloads.

**Note**
In public apps, anonymous viewers can read from and write to shared storage but cannot access private storage. Design your data model accordingly if you plan to publish your app publicly.

## Using Quick Sight datasets in an app (live data)
<a name="apps-live-data"></a>

Alongside built-in app storage, your app can query a Quick Sight in Amazon Quick dataset directly, so viewers see current data every time they open the app. The app does not copy the data. Each viewer's visuals query the dataset in real time under that viewer's own identity, so your row-level and column-level security keeps applying.

### Add a dataset to your app
<a name="apps-live-data-add"></a>

You add a dataset by asking the editing agent for it by name. There is no separate data-source menu.

1. In the app editor, tell the agent which dataset to use, for example: *Use the Sales Pipeline dataset to show pipeline by stage.*

1. The agent finds the dataset, learns its columns, and asks you to approve access to it. Approve the prompt so the agent can build against it.

1. The agent writes the visuals. Describe what you want in plain language, and name the columns you care about so it picks the right ones.

1. Publish. Each viewer approves a one-time prompt for the dataset the first time they open the app.

**Note**
Sharing an app does not share its data. Grant every viewer read access to each dataset the app uses, or share the folder that holds them, so they see data instead of an access message.

### Which datasets you can use
<a name="apps-live-data-which"></a>

Live data works with a single-table dataset, whether it is stored in SPICE or queried directly. A dataset built with the visual join editor that produces one logical table also works.
+ **Storage and engines** — Any dataset in SPICE, plus Direct Query on Redshift, Athena, Aurora PostgreSQL, PostgreSQL, Databricks, and S3 Tables. Other engines work after you import them into SPICE.
+ **Same account and Region** — The dataset and the app must be in the same account and Region.
+ **Published version** — The app queries the published version of the dataset, so publish any dataset edits you want it to use.

Some dataset shapes are not supported for live data, including multi-table (data model) datasets, composite or child datasets, and datasets that join across sources. For the full list, see [Live data (Quick Sight datasets)](apps-limitations.md#apps-limits-live-data).

### Keep your app working over time
<a name="apps-live-data-maintain"></a>

The app refers to each dataset's columns by their exact name and type at the time you built it, and it does not track changes automatically. If you rename or retype a column, or replace or delete the dataset, the visuals that use it stop working for viewers. Changing only a dataset's display name is fine. When you do change a column or dataset, reopen the app, have the agent update the affected visuals, and publish again.

### Data freshness
<a name="apps-live-data-freshness"></a>
+ **SPICE and S3 Tables** — Results are cached for up to 12 hours. A completed SPICE refresh updates what the app shows.
+ **Direct Query** — Not cached. Every open queries the source.
+ **No refresh button** — The app re-runs its queries on each page load. The header's "Last updated" date reflects the app's last edit, not data freshness.
+ **Viewer time zone** — Dates and times render in each viewer's browser time zone.

## Exporting data
<a name="apps-exporting-data"></a>

You can ask the agent to add export functionality. Apps in Quick supports exporting data as CSV, JSON, PDF, and Excel files through the bridge API. You can also have your app write data snapshots to a connected space. This serves as a backup and makes the data available to other Quick capabilities.

## Handling write approvals when AI inference is active
<a name="apps-write-approvals"></a>

When an app uses AI inference and writes data (to shared storage or through an action connector), you must review and approve each write payload. This security measure ensures that you review AI-generated content before the app persists it.

Three strategies can reduce the frequency of approval prompts:

1. **Batch writes** — Collect all items and save them under a single storage key in one operation.

1. **Separate AI from writes** — Design the app so that AI processing and data persistence happen in distinct user actions.

1. **Remove AI inference when not needed** — If your app does not use AI-generated content, ensure the AI inference integration is not registered. Without AI inference, you can choose "Allow on this app" for write operations. The permission persists across sessions.

## Accessing user information
<a name="apps-user-identity"></a>

With apps in Quick, you can access the current user's identity at runtime. This lets you personalize the app experience, display the user's name, or implement per-user logic.

Available user information includes email, first name, last name, and identity name.

**Tip**
Combine user identity with private storage to build personalized experiences such as greetings, saved preferences, bookmarks, and custom dashboards per user.
