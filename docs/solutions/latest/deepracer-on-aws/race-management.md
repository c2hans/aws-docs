---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/race-management.html
---

# Race Management
<a name="race-management"></a>

Race Management covers running **physical** racing events on your deployment. At these events, participants drive real vehicles on a real track, and a race facilitator records their lap times as the cars complete laps.

These are two different activities, held in different venues. A [race](create-manage-races.md) is a purely virtual experience: a participant submits a model they trained and the solution evaluates it in the simulator, wherever the participant happens to be. A physical racing event happens in a room, on a track: a participant loads a model they trained onto a physical car and races it, and a race facilitator times the laps.

A deployment can use both, and a participant’s trained models carry across the two. A common pattern is to train and qualify models in a community race, then race the finalists' cars on a physical track as an event.
