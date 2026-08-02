---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/types-of-users.html
---

# Types of users
<a name="types-of-users"></a>

 **Racers** are the most common type of user in DeepRacer on AWS, and any account that is created will automatically be created as a racer. Racers can learn the fundamentals of reinforcement learning; build, train, and evaluate models; and they can submit their trained models to live races that are hosted on the deployment. They can also import or export models from the deployment, allowing them to take a model to another deployment and use it there.

Racers can be promoted by an admin to either a race facilitator or to an admin (co-admin). Race facilitators and admins, in addition to their elevated permissions, also share the same abilities as racers.

 **Race facilitators** are users who have been given elevated permissions by the admin of a deployment to help with creating and managing races, including facilitating live race events — launching evaluations, managing the queue, controlling submissions, and declaring winners. Race facilitators can also view all users' trained models and download physical car models for loading onto vehicles at physical race events. Race facilitators inherit the same permissions as racers, allowing them to also create, train, and evaluate models, and submit them to community races. Admins can also perform the same functions as a race facilitator, allowing them to create and manage races, in addition to having their own elevated privileges.

 **Admins** have the highest level of permission on a given deployment of DeepRacer on AWS. Admins are able to manage the overall deployment, including managing users, resource utilization, and other operational aspects of the solution. Admins, in addition to their elevated permissions, also share the same abilities as both racers and race facilitators.

## Permissions matrix
<a name="permissions-matrix"></a>

<table>
<thead>
  <tr><th>Capability</th><th>Racer</th><th>Race Facilitator</th><th>Admin</th></tr>
</thead>
<tbody>
  <tr><td colspan="4"> ** **Models — Own** ** </td></tr>
  <tr><td>Create and train own model</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Evaluate own model</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Clone own model</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Import own model</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Export own virtual model</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Export own physical car model</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Delete own model</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td colspan="4"> ** **Models — Other users** ** </td></tr>
  <tr><td>View another user’s models</td><td>✗</td><td>✓</td><td>✓</td></tr>
  <tr><td>Download another user’s physical car model</td><td>✗</td><td>✓</td><td>✓</td></tr>
  <tr><td>Delete another user’s model(s)</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td colspan="4"> ** **Community races** ** </td></tr>
  <tr><td>View race and leaderboard</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Enter open race</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Create race</td><td>✗</td><td>✓</td><td>✓</td></tr>
  <tr><td>Edit race</td><td>✗</td><td>✓</td><td>✓</td></tr>
  <tr><td>Delete race</td><td>✗</td><td>✓</td><td>✓</td></tr>
  <tr><td colspan="4"> ** **Live races** ** </td></tr>
  <tr><td>Watch live race</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Submit model to live race</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Launch evaluation</td><td>✗</td><td>✓</td><td>✓</td></tr>
  <tr><td>Manage queue (reorder, remove, reset)</td><td>✗</td><td>✓</td><td>✓</td></tr>
  <tr><td>Toggle autolaunch</td><td>✗</td><td>✓</td><td>✓</td></tr>
  <tr><td>Open/close submissions</td><td>✗</td><td>✓</td><td>✓</td></tr>
  <tr><td>Declare winner</td><td>✗</td><td>✓</td><td>✓</td></tr>
  <tr><td>Clear leaderboard</td><td>✗</td><td>✓</td><td>✓</td></tr>
  <tr><td colspan="4"> ** **Profiles — Own** ** </td></tr>
  <tr><td>View own profile</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Edit own profile</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>Delete own profile</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td colspan="4"> ** **Profiles — Other users** ** </td></tr>
  <tr><td>View all profiles</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>View number of users</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>Delete another user’s profile</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td colspan="4"> ** **Usage - Own** ** </td></tr>
  <tr><td>View own model count</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td>View own compute usage</td><td>✓</td><td>✓</td><td>✓</td></tr>
  <tr><td colspan="4"> ** **User management** ** </td></tr>
  <tr><td>Update another user’s role</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>View another user’s basic profile attributes</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>View another user’s current compute usage</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>View another user’s queued compute usage</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>View another user’s model storage</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>Update another user’s compute usage limit</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>Update another user’s model limit</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td colspan="4"> ** **Instance management** ** </td></tr>
  <tr><td>Update the default compute usage limit for new users</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>Update the default model count limit for new users</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>Update the global compute usage limit</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>Update the global model count limit</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>View global model count</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>View global storage usage</td><td>✗</td><td>✗</td><td>✓</td></tr>
  <tr><td>View global compute usage</td><td>✗</td><td>✗</td><td>✓</td></tr>
</tbody>
</table>
