---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/create-manage-races.html
---

# Create and manage races
<a name="create-manage-races"></a>

**Note**
Only admins and race facilitators can create and manage races.

## Creating a race
<a name="creating-a-race"></a>

![Create a race screenshot #1](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_create_race_001_a.png)

![Create a race screenshot #2](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_create_race_002_a.png)

Races allow participants to test their trained models against those of other participants in a competitive setting. Races are open to all users on a given deployment to participate in, and operate by offering a pre-selected window of time during which users can submit their models. When a user submits one or more trained models to a race, those models are evaluated as they arrive and, when completed, the race leaderboard is updated to include the results of those evaluations. When the time window that the race is open for expires, the race will close and the leaderboard will become final. No submissions are allowed once a race is closed.

To create a race, from the home page, click the **Races** tab in the left sidebar. Then, click **Create race** towards the upper-right corner. You will be asked to provide the following:
+  **Race mode** — how the race is conducted:
  +  **Community race** — models are evaluated asynchronously as they are submitted; results appear on the leaderboard as evaluations complete.
  +  **Live race** — models are evaluated sequentially during a scheduled live event with video streaming; a facilitator manages the queue and controls the race in real time.
+  **Race type** — either **Time trial** or **Object avoidance**. Time trial aims to go around the track as quickly as possible while staying on track. Object avoidance aims to complete the fastest lap while avoiding objects placed on the track.
+  **Name** — give your race a name (1–64 characters).
+  **Race dates** — the period of time that your race will be open; provide a start and close date/time in 24-hour format.
+  **Live event time** — (Live race only) the scheduled date and time for the live event in 24-hour format.
+  **Competition track** — the track that your race will use.
+  **Track direction** — the direction of travel for vehicles in your race.

You can also provide a series of customizations (by expanding the **Race customizations** section):
+  **Description** - a description for your race.
+  **Ranking method** - how submissions are ranked: **Best lap time**, **Total time**, or **Average lap time**.
+  **Minimum laps** - the number of laps required for a model to pass evaluation.
+  **Maximum laps** - the total number of laps to race.
+  **Off-track penalty** - the number of seconds added to a racer’s time for driving off track.
+  **Max number of submissions per user** - the maximum number of submissions a user can submit to the race.
+  **Maximum resets per model** - (Live race only) the maximum number of times a model can be reset during the live event.

If you select an object avoidance race, you can also customize the following:
+  **Collision penalty** - the number of seconds added to a racer’s time for collision.
+  **Number of objects** - the number of objects for a racer to avoid on the track.
+  **Randomize obstacles** - whether obstacles should be randomly placed or in fixed positions.

If you opt not to randomize obstacles, you can define where the objects will be placed on the track.

When you are ready to proceed, click **Next**. This will direct you to a page where you can review your race settings. If you would like to make any changes, click the **Edit** button in the upper-right. If you would like to proceed with the configuration as shown, click **Submit**.

After clicking **Submit**, you will be directed to the race detail view, where you can view the race details, leaderboard, and any submissions you might make yourself.

## Editing a race
<a name="editing-a-race"></a>

You can edit the details of a race up until the time the race begins from the race detail view by clicking the **Edit race** button towards the upper-right corner of the screen. Once the race begins, this button will be greyed out and you will not be able to change the race configuration.

## Deleting a race
<a name="deleting-a-race"></a>

You can delete a race up until the time the race begins from the race details view by clicking the **Delete race** button towards the upper-right corner of the screen. Once the race begins, this button will be greyed out and you will not be able to delete the race.

## Cloning a race
<a name="cloning-a-race"></a>

You can clone or duplicate a race in the event that you would like to create a new race with the same configuration as a current or past race. To clone a race, click the **Races** tab in the left sidebar, then click **Manage races** in the left sidebar. Select the race you would like to clone from the table, then click **Clone race** in the upper-right corner of the table. This will bring you to the same experience that is used for creating a race, but with all of the form fields pre-populated using the values of the race being cloned. You may choose to click through all of the steps to keep all settings the same, or make any changes as desired.
