---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-mpts-channel-swap.html
---

# PUT: MPTS Channel Swap
<a name="working-with-members-of-mpts-mpts-channel-swap"></a>

Swap the channel assigned to the MPTS.

## HTTP Request and Response
<a name="working-with-members-of-mpts-mpts-channel-swap-http-request-response"></a>

### Request URL
<a name="working-with-members-of-mpts-mpts-channel-swap-http-request-response-url"></a>

```
PUT http://<Conductor IP address>/mpts/<ID of mpts>
```

### Call Header
<a name="working-with-members-of-mpts-mpts-channel-swap-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="working-with-members-of-mpts-mpts-channel-swap-http-request-response-request-body"></a>

The request body contains XML content consisting of one `mpts_members `element, consisting of the following.
+ Two `mpts_member` elements:
  + One to remove the existing channel assignment, containing the following elements.
<a name="working-with-members-of-mpts-mpts-channel-swap-http-request-response-request-body-table"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-mpts-channel-swap.html)
  + Another to add a new channel assignment, using the following elements.
<a name="working-with-members-of-mpts-mpts-channel-swap-http-request-response-request-body-table2"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-mpts-channel-swap.html)
