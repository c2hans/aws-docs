---
source_url: https://docs.aws.amazon.com/pinpoint/latest/developerguide/channels-custom-lambda-response-format.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Lambda function response format for Amazon Pinpoint
<a name="channels-custom-lambda-response-format"></a>

If you want to use the journey multivariate or yes/no split to determine the endpoint path after a custom channel activity you must structure your Lambda function response into a format that Amazon Pinpoint can understand, and then send endpoints down the correct path.

The structure of the response should be in the following format:

```
{
    <Endpoint ID 1>:{
        EventAttributes: {
            <Key1>: <Value1>,
            <Key2>: <Value2>,
            ...
        }
    },
    <Endpoint ID 2>:{
        EventAttributes: {
            <Key1>: <Value1>,
            <Key2>: <Value2>,
            ...
        }
    },
...
}
```

This will then allow you select a key and value you would like to determine the endpoints path.

![An example of a custom multivariate split.](http://docs.aws.amazon.com/pinpoint/latest/developerguide/images/journeys-yes-no-split-activity-format.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
