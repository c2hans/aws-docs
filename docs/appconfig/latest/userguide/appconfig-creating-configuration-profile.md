---
source_url: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-profile.html
---

# Creating a configuration profile in AWS AppConfig
<a name="appconfig-creating-configuration-profile"></a>

*Configuration data* is a collection of settings that influence the behavior of your application. A *configuration profile* includes, among other things, a URI that enables AWS AppConfig to locate your configuration data in its stored location and a configure type. AWS AppConfig supports the following types of configuration profiles:
+ **Feature flags**: You can use feature flags to enable or disable features within your applications or to configure different characteristics of your application features using flag attributes. AWS AppConfig stores feature flag configurations in the AWS AppConfig hosted configuration store in a feature flag format that contains data and metadata about your flags and the flag attributes. The URI for feature flag configurations is simply `hosted`.
+ **Freeform configurations**: A freeform configuration can store data in any of the following AWS services and Systems Manager tools:
  + AWS AppConfig hosted configuration store
  + Amazon Simple Storage Service
  + AWS CodePipeline
  + AWS Secrets Manager
  + AWS Systems Manager (SSM) Parameter Store
  + SSM Document Store

**Note**
If possible, we recommend hosting your configuration data in the AWS AppConfig hosted configuration store as it offers the most features and enhancements.

Here are some configuration data samples to help you better understand different types of configuration data and how they can be used in either a feature flag or free from configuration profile.

 **Feature flag configuration data**

The following feature flag configuration data enables or disables mobile payments and default payments on a per-region basis.

------
#### [ JSON ]

```
{
  "allow_mobile_payments": {
    "enabled": false
  },
  "default_payments_per_region": {
    "enabled": true
  }
}
```

------
#### [ YAML ]

```
---
allow_mobile_payments:
  enabled: false
default_payments_per_region:
  enabled: true
```

------

 **Operational configuration data**

The following freeform configuration data enforces limits on how an application processes requests.

------
#### [ JSON ]

```
{
  "throttle-limits": {
    "enabled": "true",
    "throttles": [
      {
        "simultaneous_connections": 12
      },
      {
        "tps_maximum": 5000
      }
    ],
    "limit-background-tasks": [
      true
    ]
  }
}
```

------
#### [ YAML ]

```
---
throttle-limits:
  enabled: 'true'
  throttles:
  - simultaneous_connections: 12
  - tps_maximum: 5000
  limit-background-tasks:
  - true
```

------

 **Access control list configuration data**

The following access control list freeform configuration data specifies which users or groups can access an application.

------
#### [ JSON ]

```
{
  "allow-list": {
    "enabled": "true",
    "cohorts": [
      {
        "internal_employees": true
      },
      {
        "beta_group": false
      },
      {
        "recent_new_customers": false
      },
      {
        "user_name": "Jane_Doe"
      },
      {
        "user_name": "John_Doe"
      }
    ]
  }
}
```

------
#### [ YAML ]

```
---
allow-list:
  enabled: 'true'
  cohorts:
  - internal_employees: true
  - beta_group: false
  - recent_new_customers: false
  - user_name: Jane_Doe
  - user_name: Ashok_Kumar
```

------

**Topics**
+ [Creating a feature flag configuration profile in AWS AppConfig](appconfig-creating-configuration-and-profile-feature-flags.md)
+ [Creating a free form configuration profile in AWS AppConfig](appconfig-free-form-configurations-creating.md)
+ [Creating a configuration profile for non-native data sources](appconfig-creating-configuration-profile-other-data-sources.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
