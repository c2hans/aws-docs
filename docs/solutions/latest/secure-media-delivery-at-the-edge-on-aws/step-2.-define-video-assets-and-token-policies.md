---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/step-2.-define-video-assets-and-token-policies.html
---

# Step 2. Define video assets and token policies
<a name="step-2.-define-video-assets-and-token-policies"></a>

 After the solution’s CloudFormation stack is deployed, you can define your video assets details (if you haven’t provided them as CloudFormation stack input) by following the next steps:

1.  After the solution has deployed, navigate to the DynamoDB console and **Explore items** page under **Tables.**

1.  Select the table which name starts with following string: **[Stack Name]-ApiDemoTable.**

1.  Under **Items returned** section you can add and modify the list of items which detail original video asset’s hostname with URL path and a token policy for that content. In the demo web page deployed in the solution, two video assets are requested by the use of their ID corresponding to the entries in this table. To successfully start a video playback on the website, make sure that table entry with the **ID** that equals to 1, references HLS stream and the other one with ID of 2, to DASH stream.

1.  To edit the details of the HLS stream, select an item with ID that equals to 1 and select **Action,** then choose **Edit Item.**

1.  Make sure that the **endpoint\_hostname** fields and **url\_path** are filled in correctly as instructed in the previous **HLS Stream** parameter description.

1.  Expand **token\_policy** property and modify the values of predefined properties which determine the parameters of the output token that will be created for this specific video asset.

1.  Choose **Save changes** to submit the changes.

1.  For DASH stream, repeat steps from 4 to 7.

1.  Test if API Gateway returns a valid playback URL with a secure token. Record the distribution hostname fronting API Gateway. You can find it in the launched stack output tab with a key value starting with **ApiEndpointsDistributionDomainName**. Using a utility tool like curl, make an HTTP request as follows:

 **For HLS:**

```
curl [ApiEndpointDistributionDomainName]/tokengenerate?id=1
```

 **For DASH:**

```
curl [ApiEndpointDistributionDomainName]/tokengenerate?id=2
```

 In response, you should see the playback URL comprised of video asset hostname and URL path, with the secure token added at the beginning of the original URL path.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
