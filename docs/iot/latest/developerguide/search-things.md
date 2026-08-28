---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/search-things.html
---

# Describe things
<a name="search-things"></a>

You can use the **DescribeThing** command to display more detailed information about a thing:

```
$ aws iot describe-thing --thing-name "MyLightBulb"
{
    "version": 3,
    "thingName": "MyLightBulb",
    "thingArn": "arn:aws:iot:us-east-1:123456789012:thing/MyLightBulb",
    "thingId": "12345678abcdefgh12345678ijklmnop12345678",
    "defaultClientId": "MyLightBulb",
    "thingTypeName": "StopLight",
    "attributes": {
        "model": "123",
        "wattage": "75"
    }
}
```

You can also access this API within the rules engine using the inline function `get_registry_data()`. You can use this function to dynamically access and utilize thing registry information (including attributes, thing types, and group memberships) by calling `DescribeThing` and `ListThingGroupsForThing` APIs directly within AWS IoT rules, enabling real-time message processing and routing based on your device registry data. For more information, see [`get_registry_data`](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-functions.html#iot-sql-function-get-registry_data).

For more information, see [describe-thing](https://docs.aws.amazon.com/cli/latest/reference/iot/describe-thing.html) from the AWS CLI Command Reference.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
