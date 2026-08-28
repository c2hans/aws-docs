---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/failed-token-validation.html
---

# Failed token validation
<a name="failed-token-validation"></a>

 **Issue:** Legitimate viewer request is rejected by CloudFront and returns a 401 response due to failed token validation.

 **Resolution:**

1.  Retrieve the request ID of the failed request. CloudFront Request ID value can be either found in the response header **x-amz-cf-id** when the request is made or in the CloudFront access logs under **x-edge-request-id** field.

1.  Open the CloudWatch console in the same account where the solution stack is implemented, and select `us-east-1` from the Region selector in the upper-right corner.

1.  Navigate to **Logs,** select **Log Groups** and find a log group for the CloudFront Function created by the solution. The name of the log group will be similar to `/aws/cloudfront/function/[Stack Name]_checkJWTToken`. Select the log group identified.

1.  Narrow down the time window for the log streams. Select **Search all** and in the filter panel limit the time boundaries to when the failed request was made.

1.  In **Filter events,** enter the request ID recorded in step 1.

 In the result output, you will see the log entries emitted from CloudFront Function that explains at which stage of the token verification it failed.

 **Internal signature verification failed error**

 **Issue:** When the token was generated, if the viewer attributes do not match with the attributes CloudFront function found in the event object, it results in a failed token error: **Internal signature verification failed**. When you generate the token and decide to use one or more of the following parameters: **session Id**, **headers**, **query string**, **viewer country**, **viewer region**, **viewer IP address** this will produce an internal signature build from all the selected inputs, inserted in the token payload as **intsig** claim. Based on the other claim values, CloudFront Function reproduce that input string using the selected attributes by reaching them from the event object available at runtime. If any of these attributes are missing or changed their value form when the token was generated, it will cause a mismatch of signatures and result in this error.

 **Resolution:**

1.  From the CloudFront Function Log group identify the entries associated with failed request (as specified in the description of the previous issue ), and find an entry which includes **Indirect attributes input string** which displays an input string recreated by CloudFront Function from the event object. This string will contain concatenated list of attributes with colon : as a delimiter. Take a note of it, in particular session ID which should be first element in that concatenated string.
**Note**
If you do not use session ID, we recommend that you activate it when you start using and testing the solution to facilitate troubleshooting.

1.  On the **Log Groups** page, change the region to the one where the solution stack was implemented with API module, using region selector.

1.  Find the log groups associated with the Lambda function that generates the token. Select the log group name starts with /aws/lambda/[Stack Name]\_GenerateToken.

1.  Narrow down the time window for the log streams. Select **Search all,** and in the filter panel limit the time boundaries to when the token for the viewer was made.

1.  In **Filter events**, enter the same session ID that was found in step 1 in the CloudFront Functions log stream.

1.  In the results output, find a line which includes **Input for internal signature:** which was an input string used for generating internal signature.

1.  Compare the values of both input strings and identify the attributes that do not match, or if any attribute is missing for CloudFront Function entry.

1.  Consider common causes for discrepancies in the input string values:
   +  Mismatch in viewer IP address – viewer IP address may change between the request for a token and request for video stream object as explained in the [Access token management guide](access-tokens-management-guide.md) section. In this case, consider excluding the IP address when creating the token, or include it conditionally only when it is probable that the viewer’s IP address won’t change (for example, connected TVs).
   +  Missing or different value of the viewer’s country or region – for CloudFront Function, to retrieve geolocation information about the request, Origin request policy associated with cache behavior which includes token validation, must include appropriate geolocation headers.Refer to the [Access token management guide](access-tokens-management-guide.md) section for more details.
   +  Missing or different value of the viewer’s header – make sure that the headers included in token creation won’t change during playback. For instance, when using **referer** header in the policy it is possible that the browser construct referer header differently when making request to the playback API, and when making a request to the CloudFront distribution, depending on [Referrer Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
