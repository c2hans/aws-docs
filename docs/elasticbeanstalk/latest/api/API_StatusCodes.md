---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_StatusCodes.html
---

# StatusCodes
<a name="API_StatusCodes"></a>

Represents the percentage of requests over the last 10 seconds that resulted in each type of status code response. For more information, see [Status Code Definitions](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html).

## Contents
<a name="API_StatusCodes_Contents"></a>

 ** Status2xx **
The percentage of requests over the last 10 seconds that resulted in a 2xx (200, 201, etc.) status code.
Type: Integer
Required: No

 ** Status3xx **
The percentage of requests over the last 10 seconds that resulted in a 3xx (300, 301, etc.) status code.
Type: Integer
Required: No

 ** Status4xx **
The percentage of requests over the last 10 seconds that resulted in a 4xx (400, 401, etc.) status code.
Type: Integer
Required: No

 ** Status5xx **
The percentage of requests over the last 10 seconds that resulted in a 5xx (500, 501, etc.) status code.
Type: Integer
Required: No

## See Also
<a name="API_StatusCodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/StatusCodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/StatusCodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/StatusCodes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
