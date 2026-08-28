---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-tests-permissions-policies.html
---

# Permissions and policies
<a name="device-advisor-tests-permissions-policies"></a>

You can use the following tests to determine if the policies attached to your devices’ certificates follow standard best practices.

**MQTT over WebSocket** is not supported at this time.

**"Device certificate attached policies don’t contain wildcards"**
 Validates if the permission policies associated with a device follow best practices and do not grant the device more permissions than needed.
*API test case definition:*
`EXECUTION_TIMEOUT` has a default value of 1 minute. We recommend setting a timeout of at least 30 seconds.

```
"tests":[
   {
        "name":{{"my_security_device_policies"}},
        "configuration": {
            // optional:
            "EXECUTION_TIMEOUT":"60"    // in seconds
        },
        "test": {
            "id": "Security_Device_Policies",
            "version": "0.0.0"
        }
    }
]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
