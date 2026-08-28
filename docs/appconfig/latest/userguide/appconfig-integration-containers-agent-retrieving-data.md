---
source_url: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-containers-agent-retrieving-data.html
---

# Retrieving configuration data for applications running in Amazon ECS and Amazon EKS
<a name="appconfig-integration-containers-agent-retrieving-data"></a>

You can retrieve configuration data from AWS AppConfig Agent for applications running in Amazon ECS and Amazon EKS by using an HTTP localhost call. The following examples use `curl` with an HTTP client. You can call the agent using any available HTTP client supported by your application language or available libraries.

**Note**
To retrieve configuration data if your application uses a forward slash, for example "test-backend/test-service", you will need to use URL encoding.

**To retrieve the full content of any deployed configuration**

```
$ curl "http://localhost:2772/applications/{{application_name}}/environments/{{environment_name}}/configurations/{{configuration_name}}"
```

**To retrieve a single flag and its attributes from an AWS AppConfig configuration of type `Feature Flag`**

```
$ curl "http://localhost:2772/applications/{{application_name}}/environments/{{environment_name}}/configurations/{{configuration_name}}?flag={{flag_name}}"
```

**To access multiple flags and their attributes from an AWS AppConfig configuration of type `Feature Flag`**

```
$ curl "http://localhost:2772/applications/{{application_name}}/environments/{{environment_name}}/configurations/{{configuration_name}}?flag={{flag_name_one}}&flag={{flag_name_two}}"
```

The call returns configuration metadata in HTTP headers, including the configuration version, content type, and configuration version label (if applicable). The body of the agent response contains the configuration content. Here is an example:

```
HTTP/1.1 200 OK
Configuration-Version: 1
Content-Type: application/json
Date: Tue, 18 Feb 2025 20:20:16 GMT
Content-Length: 31

My test config
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
