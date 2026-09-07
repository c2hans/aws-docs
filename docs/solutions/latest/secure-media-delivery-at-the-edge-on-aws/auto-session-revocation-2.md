---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/auto-session-revocation-2.html
---

# Auto session revocation
<a name="auto-session-revocation-2"></a>

 Auto session revocation module, when activated, regularly inspects CloudFront access logs with an objective to detect session IDs that exhibit suspicious traffic patterns in terms of request rate and composition of viewer attributes. The [Session revocation guide](session-revocation-guide.md) section provides extensive overview of what factors are accounted for when determining the suspicion score and all the inputs and settings you have control of to impact the suspicion score formula and detection threshold. If playback session gets blocked unexpectedly, complete the following steps to work backwards and identify what factored in that decision.

1.  Open DynamoDB table used as a data store for the session submitted for revocation. Table name can be found in the stack’s CloudFormation output tab associate to the key which starts with **[Stack name]-SessionToRevoke**. Locate that name in DynamoDB console in correct region on the **Explore items** page.

1.  Use Filters fields to look up the blocked session ID.
![Screeshot of Filters.](https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/image19.png)

1.  In the **Items returned** section an entry corresponding to this session will be displayed with a type attribute set to **AUTO**. Sum of **ip\_penalty**, **ip\_rate**, **referrer\_penalty**, **ua\_penalty** should equal to the final score attribute value which was above the threshold set.

1.  You can further inspect underlying SQL query which produced this entry. Take a note of the timestamp in **last\_updated** attribute which informs when the entry was submitted. You should expect the respective query to run shortly before that point in time.

1.  Navigate to the Amazon Athena console and then to **Query editor** page.

1.  Open **Recent queries** tab and look for the records run around the time indicated by the timestamp in DynamoDB table.

1.  Click on the **Execution ID** attribute which will redirect you to the query editor populating the query that was run at the time. You can run and deconstruct this query to further analyse what drove specific components that added to the final score.
