---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/types-of-users.html
---

# Types of users
<a name="types-of-users"></a>

 **Racers** are the most common type of user in DeepRacer on AWS, and any account that is created will automatically be created as a racer. Racers can learn the fundamentals of reinforcement learning; build, train, and evaluate models; and they can submit their trained models to live races that are hosted on the deployment. They can also import or export models from the deployment, allowing them to take a model to another deployment and use it there. Where the deployment is used to run [physical racing events](race-management.md), racers can view those events and the results of the runs recorded at them.

Racers can be promoted by an admin to either a race facilitator or to an admin (co-admin). Race facilitators and admins, in addition to their elevated permissions, also share the same abilities as racers.

 **Race facilitators** are users who have been given elevated permissions by the admin of a deployment to help with creating and managing races, including facilitating live race events by launching evaluations, managing the queue, controlling submissions, and declaring winners. At [physical racing events](race-management.md), race facilitators operate timekeeping: they create each racer’s run, record laps as the cars come around, and mark individual laps valid or invalid. They cannot configure the event itself or correct a recorded lap time. Both are reserved for admins. Race facilitators can also view all users' trained models and download physical car models for loading onto vehicles at physical race events. During events, race facilitators can also monitor and remotely control physical devices — restart the device service, trigger an emergency stop, and change a car’s tail-light color. For more information, see [Device management](device-management.md). Race facilitators also manage model optimization and push models to physical cars. For more information, see [Model management](model-management.md). Race facilitators inherit the same permissions as racers, allowing them to also create, train, and evaluate models, and submit them to community races. Admins can also perform the same functions as a race facilitator, allowing them to create and manage races, in addition to having their own elevated privileges.

 **Admins** have the highest level of permission on a given deployment of DeepRacer on AWS. Admins are able to manage the overall deployment, including managing users, resource utilization, and other operational aspects of the solution. Admins configure [physical racing events](race-management.md). They create an event, set its scoring rules, add and remove its tracks, advance it through its lifecycle, and delete it, and they are the only users who can correct a recorded lap time. Admins additionally onboard (activate) physical devices and organize them into fleets. For more information, see [Device management](device-management.md). Admins also manage model optimization and push models to physical cars. For more information, see [Model management](model-management.md). Admins, in addition to their elevated permissions, also share the same abilities as both racers and race facilitators.

 **Commentators** can view live data for physical races. If you are a commentator, select an event and track, then subscribe to live leaderboard, lap, and race-status updates. You can view event statistics and combined leaderboards. You cannot manage events, runs, laps, races, or models.

 **Registration managers** can register walk-up participants at physical events. If you are a registration manager, enter an email address and optional country code to create a racer account. You can edit your own profile. You cannot manage models, races, or events.

## Permissions matrix
<a name="permissions-matrix"></a>

<table>
<thead>
  <tr><th>Capability</th><th>Racer</th><th>Race facilitator</th><th>Commentator</th><th>Registration manager</th><th>Admin</th></tr>
</thead>
<tbody>
  <tr><td colspan="6"> <b> <b>Models: Own</b> </b> </td></tr>
  <tr><td>Create and train own model</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Evaluate own model</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Clone own model</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Import own model</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Export own virtual model</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Export own physical car model</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Delete own model</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>Models: Other users</b> </b> </td></tr>
  <tr><td>View another user’s models</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Download another user’s physical car model</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Delete another user’s model(s)</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>Model management</b> </b> </td></tr>
  <tr><td>Import a physical model (own)</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>View car-optimization status</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Optimize a model for car deployment</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Push a model to a car</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Download a physical car model</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>View upload status</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>Community races</b> </b> </td></tr>
  <tr><td>View race and leaderboard</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Enter open race</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Create race</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Edit race</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Delete race</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>Live races</b> </b> </td></tr>
  <tr><td>Watch live race</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Submit model to live race</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Launch evaluation</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Manage queue (reorder, remove, reset)</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Toggle autolaunch</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Open/close submissions</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Declare winner</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Clear leaderboard</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>Physical events</b> </b> </td></tr>
  <tr><td>View real-time data in Commentator view</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Register a walk-up racer</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>View events and event details</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Create event</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Edit event configuration</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Advance event to the next status</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Delete event</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>Event tracks</b> </b> </td></tr>
  <tr><td>View an event’s track list</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Add track to event</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Remove track from event</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>View combined leaderboard</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>Timekeeping</b> </b> </td></tr>
  <tr><td>View runs and their recorded laps</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Create a run for a racer</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Start, pause, end, submit, or discard a run</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Record a lap</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Mark a lap valid or invalid</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Correct a recorded lap time</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>Event statistics</b> </b> </td></tr>
  <tr><td>View event statistics</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>Device management</b> </b> </td></tr>
  <tr><td>View device list and status</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Restart device service</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Trigger an emergency stop</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Change tail-light color</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Activate a device (car or timer)</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Delete a device</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Create and manage fleets</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>Profiles: Own</b> </b> </td></tr>
  <tr><td>View own profile</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Edit own profile</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Delete own profile</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>Profiles: Other users</b> </b> </td></tr>
  <tr><td>View all profiles</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>View number of users</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Delete another user’s profile</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>Usage - Own</b> </b> </td></tr>
  <tr><td>View own model count</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>View own compute usage</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>User management</b> </b> </td></tr>
  <tr><td>Update another user’s role</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>View another user’s basic profile attributes</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>View another user’s current compute usage</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>View another user’s queued compute usage</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>View another user’s model storage</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Update another user’s compute usage limit</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Update another user’s model limit</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Invite multiple users (bulk)</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Resend a user invitation</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="6"> <b> <b>Instance management</b> </b> </td></tr>
  <tr><td>Update the default compute usage limit for new users</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Update the default model count limit for new users</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Update the global compute usage limit</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Update the global model count limit</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>View global model count</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>View global storage usage</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>View global compute usage</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
</tbody>
</table>
