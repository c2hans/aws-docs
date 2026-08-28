---
source_url: https://docs.aws.amazon.com/panorama/latest/dev/applications-manifest-parameters.html
---

End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

# Application parameters
<a name="applications-manifest-parameters"></a>

Parameters are nodes that have a basic type and can be overridden during deployment. A parameter can have a default value and a *decorator*, which instructs the application's user how to configure it.

**Parameter types**
+ `string` – A string. For example, `DEBUG`.
+ `int32` – An integer. For example, `20`
+ `float32` – A floating point number. For example, `47.5`
+ `boolean` – `true` or `false`.

The following example shows two parameters, a string and a number, which are sent to a code node as inputs.

**Example graph.json – Parameters**

```
        "nodes": [
            {
                "name": "detection_threshold",
                "interface": "float32",
                "value": 20.0,
                "overridable": true,
                "decorator": {
                    "title": "Threshold",
                    "description": "The minimum confidence percentage for a positive classification."
                }
            },
            {
                "name": "log_level",
                "interface": "string",
                "value": "INFO",
                "overridable": true,
                "decorator": {
                    "title": "Logging level",
                    "description": "DEBUG, INFO, WARNING, ERROR, or CRITICAL."
                }
            }
            ...
        ],
        "edges": [
            {
                "producer": "detection_threshold",
                "consumer": "code_node.threshold"
            },
            {
                "producer": "log_level",
                "consumer": "code_node.log_level"
            }
            ...
        ]
    }
```

You can modify parameters directly in the application manifest, or provide new values at deploy-time with overrides. For more information, see [Deploy-time configuration with overrides](applications-overrides.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
