---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/reuse-and-modify-solutions-api-gateway-workflow.html
---

# Reuse and modify solution’s API Gateway workflow
<a name="reuse-and-modify-solutions-api-gateway-workflow"></a>

 After deactivating the demo website, you can retain the API Gateway endpoints and their integrations with Lambda functions and have your own services, which interact directly with the client applications, to treat that API Gateway endpoint as an internal token service. The security of interfacing API Gateway privately relies on IAM authorization as IAM authorizer is turned on by default in API Gateway configuration fronting Lambda functions that generate the tokens, and revoke the sessions. Another aspect is integrating your CMS with the Lambda function for token generation as you must provide the inputs that define token policy for a given video asset, unless the token policy is static and same token policy template can be used. The diagram below depicts the integration model:

![Diagram of API Gateway workflow: Reuse and modify workflow.](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/image22.png)

 To integrate your existing playback services with the API module provided in the solution, review the following steps:

1.  Configure your playback services to include additional step of retrieving the token before serving playback URL back to the viewer and revoking compromised sessions. This is done through REST API calls for the API Gateway towards `/tokengenerate` and `/sessionrevoke` paths respectively. Make sure that your services communicating with API Gateway have the adequate IAM permission to invoke mentioned resource paths for the API created by the solution. You can find API ID in the CloudFormation output tab under the key which starts with: **ApiEndpointsApiEndpoint**. The API ID is a first fragment of the API hostname visible for that output in the form of `[API_id].execute-api.[region].amazonaws.com`. Example policy statement which can be used when calling API:

------
#### [ JSON ]

****

   ```
   {
       "Version":"2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "execute-api:Invoke"
               ],
               "Resource": [
                   "arn:aws:execute-api:us-east-1:{{111122223333}}:{{api-id}}/*/GET/{{pets}}/{{a1b2}}"
               ]
           }
       ]
   }
   ```

------

1. If you want to use the geolocation (country or region) when issuing the token and want to obtain viewer’s geo attributes from CloudFront (as recommended in the [Access Token Management Guide](access-tokens-management-guide.md) section), use CloudFront distribution in front of your playback services with **CloudFront-Viewer-Country** and **CloudFront-Viewer-Region** headers included in origin request policy. Next, pass these headers when calling the token API endpoints from API module. Similarly, all the header values and query string parameters that originally come from the viewer’s request and you want to incorporate in the scope of the token, must be forwarded to API Gateway in the same form as they were received by your playback services, so that Lambda function can access them accordingly.

1. Expose the metadata managed with your services to the Lambda function attached to API Gateway. At minimum, when Lambda function starts token generation process, token policy must be fetched from the metadata source as one of the inputs. Video asset hostname and URL path are also required to issue full playback URL, however if your metadata source only provide the token policy but no video asset’s hostname and URL path, only the token will be returned as Lambda output. You can explore the following metadata sharing options with in order to supply token policy and video asset’s location (as depicted on the previous diagram):

   1.  **Scenario A** - Create an integration between your CMS and DynamoDB table created under API Module, storing token policies and video assets metadata. In this approach, CMS must push the new table entries in the right format which Lambda function is able to parse. See existing items in the DynamoDB table to determine the expected structure for the new items. .

   1.  **Scenario B** - Customize Lambda function used for token generation to retrieve the required information from your CMS directly. This approach involves code changes in the Lambda function to be able to fetch necessary information, and subsequently parse it to formulate viewer context and token policy objects required to generate the token.

   1.  **Scenario C** - Provide the inputs as additional parameters when making API call. You can modify Lambda function to parse the incoming request and look for the token policy and video asset metadata in the query string parameters of that request. Apply necessary code changes into the Lambda function to include this processing logic and specify which query string attributes would be inspected accordingly.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
