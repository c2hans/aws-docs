---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/HITReferences.html
---

# HIT references using `RequesterAnnotation`
<a name="HITReferences"></a>

When building processes that leverage Amazon Mechanical Turk (Mechanical Turk), it's often valuable to keep track of identifiers associated with the data in each HIT, particularly when handling HIT responses via notifications. For example, you might want to associate your HITs with a record in a database such as Amazon DynamoDB, and want your HIT to reference the primary key of the record.

The `RequesterAnnotation` attribute is a useful option for tracking these references. When you create a HIT using `[CreateHIT](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateHITOperation.html)` or `[CreateHITWithHITType](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateHITWithHITTypeOperation.html)`, you can provide a `RequesterAnnotation` field that contains arbitrary data about each HIT. Although it is limited to 255 ASCII characters, this is generally adequate to capture identifiers that denote the origin of your data. The data provided here is only visible to the requester who created the HIT.

When you receive a notification that a HIT has been completed, you can use the `[GetHIT](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetHITOperation.html)` operation to retrieve the `RequesterAnnotation`. The identifier captured in the `RequesterAnnotation` can then be used to make updates in your database or other systems.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
