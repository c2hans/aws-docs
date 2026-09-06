---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-pass-through-aws-elemental-live.html
---

# Pass Through to AWS Elemental Live
<a name="commands-pass-through-aws-elemental-live"></a>

| Nickname | Action | Signature | Description |
| --- | --- | --- | --- |
| POST Live action | POST |  http://<Conductor IP address>/channels/<ID of channel>/live\_events/<action> | Pass an AWS Elemental Live API event command to the Live node via the Conductor Live API. |
| GET System Status | GET | http://<Conductor IP address>/nodes/<ID of node>/system\_status | Get status information on an AWS Elemental Live node in the cluster. |
| GET Inputs | GET | http://<Conductor IP address> /channels/<ID of channel>/live\_events/inputs | Get the ID of an event input. |
