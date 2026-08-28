---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-dev/DeleteSessions.html
---

# DeleteSessions
<a name="DeleteSessions"></a>

Deletes the specified Amazon DCV session and removes it from the Broker's cache.

**Topics**
+ [Request parameters](#request)
+ [Response parameters](#response)
+ [Example](#example)

## Request parameters
<a name="request"></a>

**`SessionId`**
The ID of the session to delete.
Type: String
Required: Yes

**`Owner`**
The owner of the session to delete.
Type: String
Required: Yes

**`Force`**
Removes a session from the Broker's cache with attempting to delete it from the Amazon DCV server. This is useful for removing outdated sessions from the Broker's cache. For example, if a Amazon DCV server was stopped, but the sessions are still registered on the Broker, use this flag to purge the sessions from the Broker's cache.
Keep in mind that if the session is still active, it is re-cached by the Broker.
Valid values: `true` \| `false`
Type: Boolean
Required: No

## Response parameters
<a name="response"></a>

**`SessionId`**
The ID of the session

**`State`**
Only returned if the sessions were successfully deleted. Indicates the current state of the session. If the request completes successfully, the session transitions to the `DELETING` state. It could take a few minutes for the session to be deleted. When it has been deleted, the state transitions from `DELETING` to `DELETED`.

**`FailureReason`**
Only returned if some sessions could not be deleted. Indicates why the session could not be deleted.

## Example
<a name="example"></a>

------
#### [ Python ]

**Request**
The following example deletes two sessions—a session with an ID of `SessionId123` that is owned by `user1`, and a session with an ID of `SessionIdabc` that is owned by `user99`.

```
from swagger_client.models.delete_session_request_data import DeleteSessionRequestData

def get_sessions_api():
    api_instance = swagger_client.SessionsApi(swagger_client.ApiClient(get_client_configuration()))
    set_request_headers(api_instance.api_client)
    return api_instance

def delete_sessions(sessions_to_delete, force=False):
    delete_sessions_request = list()
    for session_id, owner in sessions_to_delete:
        a_request = DeleteSessionRequestData(session_id=session_id, owner=owner, force=force)
        delete_sessions_request.append(a_request)

    print('Delete Sessions Request:', delete_sessions_request)
    api_instance = get_sessions_api()
    api_response = api_instance.delete_sessions(body=delete_sessions_request)
    print('Delete Sessions Response', api_response)

def main():
    delete_sessions([('SessionId123', 'an owner user1'), ('SessionIdabc', 'user99')])
```

**Response**
The following is the sample output. `SessionId123` was successfully deleted, while `SessionIdabc` could not be deleted.

```
{
    "RequestId": "10311636-df90-4cd1-bcf7-474e9675b7cd",
    "SuccessfulList": [
        {
            "SessionId": "SessionId123",
            "State": "DELETING"
        }
    ],
    "UnsuccessfulList": [
        {
            "SessionId": "SessionIdabc",
            "FailureReason": "The requested dcvSession does not exist"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
