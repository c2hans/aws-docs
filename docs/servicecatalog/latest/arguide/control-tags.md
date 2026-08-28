---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/arguide/control-tags.html
---

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Controlling the resources associated to applications
<a name="control-tags"></a>

 This topic includes policy templates that you can use to control how tag key-value pairs are associated to applications.

 The following policy templates are organized by scenario and include values that can be replaced with your information.

 ** Sample policy: Stack only association **

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
                "servicecatalog:*",
                "cloudformation:DescribeStacks",
                "resource-groups:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": "servicecatalog:AssociateResource",
            "Resource": "arn:aws:servicecatalog:*:*:*",
            "Condition": {
                "StringNotEquals": {
                    "servicecatalog:ResourceType": "{{CFN_STACK}}"
                }
            }
        }
    ]
}
```

------

 ** Sample policy: Stack association that allows a specific stack name **

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
                "servicecatalog:*",
                "cloudformation:DescribeStacks",
                "resource-groups:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "servicecatalog:AssociateResource"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "servicecatalog:ResourceType": "{{CFN_STACK}}"
                }
            }
        }
    ]
}
```

------

 ** Sample policy: Stack association that allows multiple specific stack names **

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
                "servicecatalog:*",
                "cloudformation:DescribeStacks",
                "resource-groups:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "servicecatalog:AssociateResource"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "servicecatalog:ResourceType": "{{CFN_STACK}}"
                }
            }
        }
    ]
}
```

------

 ** Sample policy: Tag value association that denies a specific tag query value while allowing other tag queries **

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
                "servicecatalog:*",
                "cloudformation:DescribeStacks",
                "resource-groups:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "servicecatalog:AssociateResource"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "servicecatalog:ResourceType": "{{TAG_QUERY}}"
                }
            }
        }
    ]
}
```

------

 ** Sample policy: Allow tag query association only **

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
                "servicecatalog:*",
                "cloudformation:DescribeStacks",
                "resource-groups:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "servicecatalog:AssociateResource"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "servicecatalog:ResourceType": "{{TAG_QUERY}}"
                }
            }
        }
    ]
}
```

------

 ** Sample policy: Allow tag query association/deny specific tag query values **

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
                "servicecatalog:*",
                "cloudformation:DescribeStacks",
                "resource-groups:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "servicecatalog:AssociateResource"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "servicecatalog:ResourceType": "{{CFN_STACK}}"
                }
            }
        },
        {
            "Effect": "Deny",
            "Action": [
                "servicecatalog:AssociateResource"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "servicecatalog:ResourceType": ["{{TAG_QUERY}}"]
                }
            }
        }
    ]
}
```

------

 ** Sample policy: Allow specific tag query value and specific stack **

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
                "servicecatalog:*",
                "cloudformation:DescribeStacks",
                "resource-groups:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "servicecatalog:AssociateResource"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "servicecatalog:AssociateResource"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "servicecatalog:ResourceType": "{{CFN_STACK}}"
                }
            }
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
