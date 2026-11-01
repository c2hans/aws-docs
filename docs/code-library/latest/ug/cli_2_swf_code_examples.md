---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_swf_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon SWF examples using AWS CLI
<a name="cli_2_swf_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon SWF.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `count-closed-workflow-executions`
<a name="swf_CountClosedWorkflowExecutions_cli_2_topic"></a>

The following code example shows how to use `count-closed-workflow-executions`.

**AWS CLI**
**To count closed workflow executions**
The following `count-closed-workflow-executions` example retrieves the number of closed workflow executions for a given domain. You can specify filters to count specific classes of executions.
The `--domain` and *either* `--close-time-filter` or `--start-time-filter` arguments are required. All other arguments are optional.

```
aws swf count-closed-workflow-executions \
    --domain {{DataFrobtzz}} \
    --close-time-filter "{ \"latestDate\" : 1377129600, \"oldestDate\" : 1370044800 }"
```
Output:

```
{
    "count": 2,
    "truncated": false
}
```
If "truncated" is `true`, then "count" represents the maximum number that can be returned by Amazon SWF. Any further results are truncated.
To reduce the number of results returned, you can:
modify the `--close-time-filter` or `--start-time-filter` values to narrow the time range that is searched. Eachof these is mutually exclusive: You can specify *only one of these* in a request.use the `--close-status-filter`, `--execution-filter`, `--tag-filter` or `--type-filter` arguments to furtherfilter the results. However, these arguments are also mutually exclusive.
For more information, see [Workflow execution closure in Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-workflow-exec-closure.html) in the *Amazon Simple Workflow Service Developer Guide*.
+  For API details, see [CountClosedWorkflowExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/count-closed-workflow-executions.html) in *AWS CLI Command Reference*.

### `count-open-workflow-executions`
<a name="swf_CountOpenWorkflowExecutions_cli_2_topic"></a>

The following code example shows how to use `count-open-workflow-executions`.

**AWS CLI**
**To count open workflow executions**
The following `count-open-workflow-executions` example retrieves the number of open workflow executions for a given domain. You can specify filters to count specific classes of executions.
The `--domain` and `--start-time-filter` arguments are required. All other arguments are optional.

```
aws swf count-open-workflow-executions \
    --domain {{DataFrobtzz}} \
    --start-time-filter "{ \"latestDate\" : 1377129600, \"oldestDate\" : 1370044800 }"
```
Output:

```
{
    "count": 4,
    "truncated": false
}
```
If "truncated" is `true`, then "count" represents the maximum number that can be returned by Amazon SWF. Any further results are truncated.
To reduce the number of results returned, you can:
modify the `--start-time-filter` values to narrow the time range that is searched.use the `--close-status-filter`, `--execution-filter`, `--tag-filter` or `--type-filter` arguments to furtherfilter the results. Each of these is mutually exclusive: You can specify *only one of these* in a request.
For more information, see [Life cycle of a Amazon SWF workflow](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-workflow-exec-lifecycle.html) in the *Amazon Simple Workflow Service Developer Guide*.
+  For API details, see [CountOpenWorkflowExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/count-open-workflow-executions.html) in *AWS CLI Command Reference*.

### `deprecate-domain`
<a name="swf_DeprecateDomain_cli_2_topic"></a>

The following code example shows how to use `deprecate-domain`.

**AWS CLI**
**To deprecate a domain**
The following `deprecate-domain` example deprecates a domain. You can still see a deprecated domain, but cannot create new workflow executions or register types on it. The command has a sole required parameter, `--name`, which takes the name of the domain to deprecate.

```
aws swf deprecate-domain \
    --name {{MyNeatNewDomain}}
```
This command produces no output.
As with `register-domain`, no output is returned. If you use `list-domains` to view the registered domains, however, you will see that the domain has been deprecated and no longer appears in the returned data.

```
aws swf list-domains \
    --registration-status {{REGISTERED}}
```
Output:

```
{
    "domainInfos": [
        {
            "status": "REGISTERED",
            "name": "DataFrobotz"
        },
        {
            "status": "REGISTERED",
            "name": "erontest"
        }
    ]
}
```
If you use `--registration-status DEPRECATED` with `list-domains`, you will see your deprecated domain.

```
aws swf list-domains \
    --registration-status {{DEPRECATED}}
```
Output:

```
{
    "domainInfos": [
        {
            "status": "DEPRECATED",
            "name": "MyNeatNewDomain"
        }
    ]
}
```
You can still use `describe-domain` to get information about a deprecated domain.

```
aws swf describe-domain \
    --name {{MyNeatNewDomain}}
```
Output:

```
{
    "domainInfo": {
        "status": "DEPRECATED",
        "name": "MyNeatNewDomain"
    },
    "configuration": {
        "workflowExecutionRetentionPeriodInDays": "0"
    }
}
```
For more information, see [Domains in Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-domains.html) in the *Amazon Simple Workflow Service Developer Guide*.
+  For API details, see [DeprecateDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/deprecate-domain.html) in *AWS CLI Command Reference*.

### `describe-domain`
<a name="swf_DescribeDomain_cli_2_topic"></a>

The following code example shows how to use `describe-domain`.

**AWS CLI**
**To get information about a domain**
The following `describe-domain` example gets detailed information about a particular domain. There is one required parameter: `--name`, which takes the name of the domain you want information about.

```
aws swf describe-domain \
    --name {{DataFrobotz}}
```
Output:

```
{
    "domainInfo": {
        "status": "REGISTERED",
        "name": "DataFrobotz"
    },
    "configuration": {
        "workflowExecutionRetentionPeriodInDays": "1"
    }
}
```
You can also use `describe-domain` to get information about deprecated domains.

```
aws swf describe-domain \
    --name {{MyNeatNewDomain}}
```
Output:

```
{
    "domainInfo": {
        "status": "DEPRECATED",
        "name": "MyNeatNewDomain"
    },
    "configuration": {
        "workflowExecutionRetentionPeriodInDays": "0"
    }
}
```
For more information, see [Domains in Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-domains.html) in the *Amazon Simple Workflow Service Developer Guide*.
+  For API details, see [DescribeDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-domain.html) in *AWS CLI Command Reference*.

### `list-activity-types`
<a name="swf_ListActivityTypes_cli_2_topic"></a>

The following code example shows how to use `list-activity-types`.

**AWS CLI**
**To list activity types**
The following `list-activity-types` example gets a list of the activity types for a domain. The `--domain` and `--registration-status` arguments are required.

```
aws swf list-activity-types \
    --domain {{DataFrobtzz}} \
    --registration-status {{REGISTERED}}
```
Output:

```
{
    "typeInfos": [
        {
            "status": "REGISTERED",
            "creationDate": 1371454150.451,
            "activityType": {
                "version": "1",
                "name": "confirm-user-email"
            },
            "description": "subscribe confirm-user-email activity"
        },
        {
            "status": "REGISTERED",
            "creationDate": 1371454150.709,
            "activityType": {
                "version": "1",
                "name": "confirm-user-phone"
            },
            "description": "subscribe confirm-user-phone activity"
        },
        {
            "status": "REGISTERED",
            "creationDate": 1371454149.871,
            "activityType": {
                "version": "1",
                "name": "get-subscription-info"
            },
            "description": "subscribe get-subscription-info activity"
        },
        {
            "status": "REGISTERED",
            "creationDate": 1371454150.909,
            "activityType": {
                "version": "1",
                "name": "send-subscription-success"
            },
            "description": "subscribe send-subscription-success activity"
        },
        {
            "status": "REGISTERED",
            "creationDate": 1371454150.085,
            "activityType": {
                "version": "1",
                "name": "subscribe-user-sns"
            },
            "description": "subscribe subscribe-user-sns activity"
        }
    ]
}
```
You can use the `--name` argument to select only activity types with a particular name.

```
aws swf list-activity-types \
    --domain {{DataFrobtzz}} \
    --registration-status {{REGISTERED}} \
    --name {{"send-subscription-success"}}
```
Output:

```
{
    "typeInfos": [
        {
            "status": "REGISTERED",
            "creationDate": 1371454150.909,
            "activityType": {
                "version": "1",
                "name": "send-subscription-success"
            },
            "description": "subscribe send-subscription-success activity"
        }
    ]
}
```
To retrieve results in pages, you can set the `--maximum-page-size` argument. If more results are returned than will fit in a page of results, a "nextPageToken" will be returned in the result set.

```
aws swf list-activity-types \
    --domain {{DataFrobtzz}} \
    --registration-status {{REGISTERED}} \
    --maximum-page-size {{2}}
```
Output:

```
{
    "nextPageToken": "AAAAKgAAAAEAAAAAAAAAA1Gp1BelJq+PmHvAnDxJYbup8+0R4LVtbXLDl7QNY7C3OpHo9Sz06D/GuFz1OyC73umBQ1tOPJ/gC/aYpzDMqUIWIA1T9W0s2DryyZX4OC/6Lhk9/o5kdsuWMSBkHhgaZjgwp3WJINIFJFdaSMxY2vYAX7AtRtpcqJuBDDRE9RaRqDGYqIYUMltarkiqpSY1ZVveBasBvlvyUb/WGAaqehiDz7/JzLT/wWNNUMOd+Nhe",
    "typeInfos": [
        {
            "status": "REGISTERED",
            "creationDate": 1371454150.451,
            "activityType": {
                "version": "1",
                "name": "confirm-user-email"
            },
            "description": "subscribe confirm-user-email activity"
        },
        {
            "status": "REGISTERED",
            "creationDate": 1371454150.709,
            "activityType": {
                "version": "1",
                "name": "confirm-user-phone"
            },
            "description": "subscribe confirm-user-phone activity"
        }
    ]
}
```
You can pass the nextPageToken value to the next call to `list-activity-types` in the `--next-page-token` argument, retrieving the next page of results.

```
aws swf list-activity-types \
    --domain {{DataFrobtzz}} \
    --registration-status {{REGISTERED}} \
    --maximum-page-size {{2}} \
    --next-page-token {{"AAAAKgAAAAEAAAAAAAAAA1Gp1BelJq+PmHvAnDxJYbup8+0R4LVtbXLDl7QNY7C3OpHo9Sz06D/GuFz1OyC73umBQ1tOPJ/gC/aYpzDMqUIWIA1T9W0s2DryyZX4OC/6Lhk9/o5kdsuWMSBkHhgaZjgwp3WJINIFJFdaSMxY2vYAX7AtRtpcqJuBDDRE9RaRqDGYqIYUMltarkiqpSY1ZVveBasBvlvyUb/WGAaqehiDz7/JzLT/wWNNUMOd+Nhe"}}
```
Output:

```
{
    "nextPageToken": "AAAAKgAAAAEAAAAAAAAAAw+7LZ4GRZPzTqBHsp2wBxWB8m1sgLCclgCuq3J+h/m3+vOfFqtkcjLwV5cc4OjNAzTCuq/XcylPumGwkjbajtqpZpbqOcVNfjFxGoi0LB2Olbvv0krbUISBvlpFPmSWpDSZJsxg5UxCcweteSlFn1PNSZ/MoinBZo8OTkjMuzcsTuKOzH9wCaR8ITcALJ3SaqHU3pyIRS5hPmFA3OLIc8zaAepjlaujo6hntNSCruB4",
    "typeInfos": [
        {
            "status": "REGISTERED",
            "creationDate": 1371454149.871,
            "activityType": {
                "version": "1",
                "name": "get-subscription-info"
            },
            "description": "subscribe get-subscription-info activity"
        },
        {
            "status": "REGISTERED",
            "creationDate": 1371454150.909,
            "activityType": {
                "version": "1",
                "name": "send-subscription-success"
            },
            "description": "subscribe send-subscription-success activity"
        }
    ]
}
```
If there are still more results to return, "nextPageToken" will be returned with the results. When there are no more pages of results to return, "nextPageToken" will *not* be returned in the result set.
You can use the `--reverse-order` argument to reverse the order of the returned results. This also affects paged results.

```
aws swf list-activity-types \
    --domain {{DataFrobtzz}} \
    --registration-status {{REGISTERED}} \
    --maximum-page-size {{2}} \
    --reverse-order
```
Output:

```
{
    "nextPageToken": "AAAAKgAAAAEAAAAAAAAAAwXcpu5ePSyQkrC+8WMbmSrenuZC2ZkIXQYBPB/b9xIOVkj+bMEFhGj0KmmJ4rF7iddhjf7UMYCsfGkEn7mk+yMCgVc1JxDWmB0EH46bhcmcLmYNQihMDmUWocpr7To6/R7CLu0St1gkFayxOidJXErQW0zdNfQaIWAnF/cwioBbXlkz1fQzmDeU3M5oYGMPQIrUqkPq7pMEW0q0lK5eDN97NzFYdZZ/rlcLDWPZhUjY",
    "typeInfos": [
        {
            "status": "REGISTERED",
            "creationDate": 1371454150.085,
            "activityType": {
                "version": "1",
                "name": "subscribe-user-sns"
            },
            "description": "subscribe subscribe-user-sns activity"
        },
        {
            "status": "REGISTERED",
            "creationDate": 1371454150.909,
            "activityType": {
                "version": "1",
                "name": "send-subscription-success"
            },
            "description": "subscribe send-subscription-success activity"
        }
    ]
}
```
For more information, see [Registering an Activity Type with Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-register-activity.html) in the *Amazon Simple Workflow Service Developer Guide*.
+  For API details, see [ListActivityTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-activity-types.html) in *AWS CLI Command Reference*.

### `list-domains`
<a name="swf_ListDomains_cli_2_topic"></a>

The following code example shows how to use `list-domains`.

**AWS CLI**
**Example 1: To list your registered domains**
The following `list-domains` example lists the `REGISTERED` SWF domains that you have registered for your account.

```
aws swf list-domains \
    --registration-status {{REGISTERED}}
```
Output:

```
{
    "domainInfos": [
        {
            "status": "REGISTERED",
            "name": "DataFrobotz"
        },
        {
            "status": "REGISTERED",
            "name": "erontest"
        }
    ]
}
```
For more information, see [Domains in Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-domains.html) in the *Amazon Simple Workflow Service Developer Guide*.
**Example 2: To list your deprecated domains**
The following `list-domains` example lists the `DEPRECATED` SWF domains that you have registered for your account. Deprecated domains are domains that can not register new workflows or activities, but that can still be queried.

```
aws swf list-domains \
    --registration-status {{DEPRECATED}}
```
Output:

```
{
    "domainInfos": [
        {
            "status": "DEPRECATED",
            "name": "MyNeatNewDomain"
        }
    ]
}
```
For more information, see [Domains in Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-domains.html) in the *Amazon Simple Workflow Service Developer Guide*.
**Example 3: To list the first page of registered domains**
The following `list-domains` example lists the first page `REGISTERED` SWF domains that you have registered for your account using the `--maximum-page-size` option.

```
aws swf list-domains \
    --registration-status {{REGISTERED}} \
    --maximum-page-size {{1}}
```
Output:

```
{
    "domainInfos": [
        {
            "status": "REGISTERED",
            "name": "DataFrobotz"
        }
    ],
    "nextPageToken": "AAAAKgAAAAEAAAAAAAAAA2QJKNtidVgd49TTeNwYcpD+QKT2ynuEbibcQWe2QKrslMGe63gpS0MgZGpcpoKttL4OCXRFn98Xif557it+wSZUsvUDtImjDLvguyuyyFdIZtvIxIKEOPm3k2r4OjAGaFsGOuVbrKljvla7wdU7FYH3OlkNCP8b7PBj9SBkUyGoiAghET74P93AuVIIkdKGtQ=="
}
```
For more information, see [Domains in Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-domains.html) in the *Amazon Simple Workflow Service Developer Guide*.
**Example 4: To list the specified single page of registered domains**
The following `list-domains` example lists the first page `REGISTERED` SWF domains that you have registered for your account using the `--maximum-page-size` option.
When you make the call again, this time supplying the value of `nextPageToken` in the `--next-page-token` argument, you'll get another page of results.

```
aws swf list-domains \
    --registration-status {{REGISTERED}} \
    --maximum-page-size {{1}} \
    --next-page-token {{"AAAAKgAAAAEAAAAAAAAAA2QJKNtidVgd49TTeNwYcpD+QKT2ynuEbibcQWe2QKrslMGe63gpS0MgZGpcpoKttL4OCXRFn98Xif557it+wSZUsvUDtImjDLvguyuyyFdIZtvIxIKEOPm3k2r4OjAGaFsGOuVbrKljvla7wdU7FYH3OlkNCP8b7PBj9SBkUyGoiAghET74P93AuVIIkdKGtQ=="}}
```
Output:

```
{
    "domainInfos": [
        {
            "status": "REGISTERED",
            "name": "erontest"
        }
    ]
}
```
When there are no further pages of results to retrieve, `nextPageToken` will not be returned in the results.
For more information, see [Domains in Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-domains.html) in the *Amazon Simple Workflow Service Developer Guide*.
+  For API details, see [ListDomains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-domains.html) in *AWS CLI Command Reference*.

### `list-workflow-types`
<a name="swf_ListWorkflowTypes_cli_2_topic"></a>

The following code example shows how to use `list-workflow-types`.

**AWS CLI**
**To list workflow types**
The following `list-workflow-types` example gets a list of the workflow types for a domain. The `--domain` and `--registration-status` arguments are required.

```
aws swf list-workflow-types \
    --domain {{DataFrobtzz}} \
    --registration-status {{REGISTERED}}
```
Output:

```
{
    "typeInfos": [
        {
            "status": "REGISTERED",
            "creationDate": 1371454149.598,
            "description": "DataFrobtzz subscribe workflow",
            "workflowType": {
                "version": "v3",
                "name": "subscribe"
            }
        }
    ]
}
```
As with `list-activity-types`, you can use the `--name` argument to select only workflow types with a particular name, and use the `--maximum-page-size` argument in coordination with `--next-page-token` to page results. To reverse the order in which results are returned, use `--reverse-order`.
For more information, see [Basic workflow concepts in Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-basic.html) in the *Amazon Simple Workflow Service Developer Guide*.
+  For API details, see [ListWorkflowTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-workflow-types.html) in *AWS CLI Command Reference*.

### `register-domain`
<a name="swf_RegisterDomain_cli_2_topic"></a>

The following code example shows how to use `register-domain`.

**AWS CLI**
**To register a domain**
The following `register-domain` example registers a new domain. There are two required parameters, `--name`, which takes the domain name, and `--workflow-execution-retention-period-in-days`, which takes an integer to specify the number of days to retain workflow execution data on this domain, up to a maximum period of 90 days (for more information, see the SWF FAQ <https://aws.amazon.com/swf/faqs/\#retain\_limit>). Workflow execution data will not be retained after the specified number of days have passed.

```
aws swf register-domain \
    --name {{MyNeatNewDomain}} \
    --workflow-execution-retention-period-in-days {{0}}
```
This command produces no output.
When you register a domain, nothing is returned, but you can use `swf list-domains` or `swf describe-domain` to see the new domain.

```
aws swf list-domains \
    --registration-status {{REGISTERED}}
```
Output:

```
{
    "domainInfos": [
        {
            "status": "REGISTERED",
            "name": "DataFrobotz"
        },
        {
            "status": "REGISTERED",
            "name": "MyNeatNewDomain"
        },
        {
            "status": "REGISTERED",
            "name": "erontest"
        }
    ]
}
```
The following example uses `swf describe-domain` to see the new domain.

```
aws swf describe-domain \
    --name {{MyNeatNewDomain}}
```
Output:

```
{
    "domainInfo": {
        "status": "REGISTERED",
        "name": "MyNeatNewDomain"
    },
    "configuration": {
        "workflowExecutionRetentionPeriodInDays": "0"
    }
}
```
For more information, see [Domains in Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-domains.html) in the *Amazon Simple Workflow Service Developer Guide*.
+  For API details, see [RegisterDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-domain.html) in *AWS CLI Command Reference*.

### `register-workflow-type`
<a name="swf_RegisterWorkflowType_cli_2_topic"></a>

The following code example shows how to use `register-workflow-type`.

**AWS CLI**
**To register a workflow type**
The following `register-workflow-type` example registers a workflow type.

```
aws swf register-workflow-type \
    --domain {{DataFrobtzz}} \
    --name {{"MySimpleWorkflow"}} \
    --workflow-version {{"v1"}}
```
This command produces no output.
On an error (for example, if you try to register the same workflow typetwice, or specify a domain that doesn't exist) you will get a response in JSON.

```
{
    "message": "WorkflowType=[name=MySimpleWorkflow, version=v1]",
    "__type": "com.amazonaws.swf.base.model#TypeAlreadyExistsFault"
}
```
The `--domain`, `--name` and `--workflow-version` are required. You can also set the workflow description, timeouts, and child workflow policy.
For more information, see [Basic workflow concepts in Amazon SWF](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-basic.html) in the *Amazon Simple Workflow Service Developer Guide*.
+  For API details, see [RegisterWorkflowType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-workflow-type.html) in *AWS CLI Command Reference*.
