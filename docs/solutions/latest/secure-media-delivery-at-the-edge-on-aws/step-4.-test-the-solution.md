---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/step-4.-test-the-solution.html
---

# Step 4. Test the solution
<a name="step-4.-test-the-solution"></a>

 After all the components and configurations that integrate your video delivery workload with the solution are in place, you can use the demo website to test the end-to-end workflow.

1.  From the **Outputs** tab of the solution’s CloudFormation stack, refer to the output starting with **ApiEndpointsDistributionDomainName** and select the link which will take you to the demo website.

1.  You will see two buttons, one for each format – HLS and DASH, each corresponding to the video assets with ID attributes 1 and 2 respectively, configured previously in video assets DynamoDB table.

1.  Choose either **HLS** or **DASH** to initiate an API call from the web client requesting playback URL and secure token.

1.  If the playback URL and token were retrieved successfully the video playback will start. You can switch between the streams at any time.

1.  Upon successful API request that returned a playback URL with the token, a demo website displays the details about the content of the token, showing the claims included in its body. These can be helpful in performing troubleshooting activities.

1.  To test manual session revocation, select **Revoke current session** to see how current playback session will get blocked when the session ID corresponding to the used token will start being blocked by AWS WAF.

1.  If you need to generate a new token and refresh current playback session, select the **Refresh token** option on the website.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
