---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-swap-allocation.html
---

# PUT: Swap Allocation
<a name="working-with-mpts-swap-allocation"></a>

Swap the allocation values (values of the `allocation_message_priority` element) in two related MPTS outputs.

This command is useful when you have set up two MPTS outputs for output listening, in order to support MPTS output redundancy. The two MPTS outputs are a “redundant pair.” This output listening feature is set up as follows:
+ Both MPTS outputs are identical with one exception: one of the outputs has its allocation\_message\_priority set to “primary” while the other has it set to “secondary.” Importantly, the two MPTS outputs contain exactly the same SPTS programs and the same destination, so that they are nearly duplicates of each other.
+ On the MPTS that is the “secondary”, the `output_listening` element is set to true and the `output_listening_interval` element has a value. In this way, the secondary MPTS output is set up to listen to the primary MPTS output.

This Swap Allocation command lets you switch the roles of the two pairs of MPTS outputs. This switch is achieved by `simultaneously `setting the allocation\_message\_priority value on the primary output to “secondary” and the value on the secondary output to “primary.”

For this command to succeed, the following conditions must be met:
+ The two MPTS outputs must be identical in all values except for the **allocation\_message\_priority** element.
+ The allocation\_message\_priority value must be “primary” for one output and “secondary” for the other.
+ Every SPTS program in the two MPTS outputs must be used only in these two MPTS outputs.

## HTTP Request and Response
<a name="working-with-mpts-swap-allocation-http-request-response"></a>

### Request URL
<a name="working-with-mpts-swap-allocation-http-request-response-url"></a>

```
PUT http://<Conductor IP address>/mpts/swap_allocaton_priority
```

### Call Header
<a name="working-with-mpts-swap-allocation-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="working-with-mpts-swap-allocation-http-request-response-request-body"></a>

The request body contains XML content consisting of one `mpts_ids `element with the following.
+ Two `mpts_id` elements, each containing the ID of an MPTS output.
