---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/step-3.-prepare-your-cloudfront-distributions.html
---

# Step 3. Prepare your CloudFront distributions
<a name="step-3.-prepare-your-cloudfront-distributions"></a>

 After deploying the CloudFormation stack and configuring DynamoDB table with inputs needed to generate the token, follow the additional steps below to integrate the Secure Media Delivery at the Edge on AWS solution with the existing CloudFront distributions used to deliver video streams.

1.  Validate if the defined cache behaviors related to the objects which are supposed to be token protected have their path pattern set correctly as described in the [Design considerations](cloudfront-prerequisites.md) section.

1.  When using viewer’s geolocation as one of the token attributes, make sure the same cache behaviors have origin request policies attached, which include CloudFront-Viewer-Country and CloudFront-Viewer-Country-Region headers.

1.  For each cache behavior subject to token protection, associate a function created when solution’s stack was launched. From CloudFront’s console, open distribution settings and navigate to a specific cache behavior configuration. In **Function associations** section, from **Viewer Request** select **CloudFront Function** event and form **Function ARN / Name**, then select the **[Stack Name]\_checkJWTToken** function.
![Screenshot of optional function associations.](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/image14.png)

1.  Choose **Save Changes** and repeat the above steps for each distribution and cache behavior where token validation mechanism must be in place.

1.  If you intend to use manual session revocation, add a WAF rule group created for storing session IDs (identified to be blocked) to the web ACL associated with the CloudFront distribution used for streaming video content. On the web ACL page, select **Global (CloudFront)**, then select the web ACL associated with your CloudFront distribution and select the **Rules** tab then choose **Add Rules** > **Add my own rules and rule groups.**

1.  In the **rule type** setting, select **Rule group** and enter a name to the rule you are defining. Under **Rule Group**, select the **[Stack\_Name]\_BlockSessions** rule group from the dropdown list .

1.  Choose **Add rule** and adjust the priority of this rule group within the web ACL, then choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
