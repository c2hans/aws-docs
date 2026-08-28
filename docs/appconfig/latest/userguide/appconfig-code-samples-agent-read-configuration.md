---
source_url: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-code-samples-agent-read-configuration.html
---

# Using AWS AppConfig Agent to read a freeform configuration profile
<a name="appconfig-code-samples-agent-read-configuration"></a>

Each of the following samples includes comments about the actions performed by the code.

------
#### [ Java ]

```
public void retrieveConfigFromAgent() throws Exception {
        /*
        In this sample, we will retrieve configuration data from the AWS AppConfig Agent.
        The agent is a sidecar process that handles retrieving configuration data from AppConfig
        for you in a way that implements best practices like configuration caching.

        For more information about the agent, see [How to use AWS AppConfig Agent](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use.html)
        */

        // The agent runs a local HTTP server that serves configuration data
        // Make a GET request to the agent's local server to retrieve the configuration data
        URL url = new URL("http://localhost:2772/applications/MyDemoApp/environments/Beta/configurations/MyConfigProfile");
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        // To enable entity-based deployments, add the Entity-Id header to the request:
        // con.setRequestProperty("Entity-Id", entityId);
        StringBuilder content;
        try (BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()))) {
            content = new StringBuilder();
            int ch;
            while ((ch = in.read()) != -1) {
                content.append((char) ch);
            }
        }
        con.disconnect();
        System.out.println("Configuration from agent via HTTP: " + content);
    }
```

------
#### [ Python ]

```
# in this sample, we will retrieve configuration data from the AWS AppConfig Agent.
# the agent is a sidecar process that handles retrieving configuration data from AWS AppConfig
# for you in a way that implements best practices like configuration caching.
#
# for more information about the agent, see
# [How to use AWS AppConfig Agent](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use.html)
#

import requests

application_name = 'MyDemoApp'
environment_name = 'MyEnvironment'
config_profile_name = 'MyConfigProfile'

# To enable entity-based deployments, add the Entity-Id header to the request:
# response = requests.get(f"http://localhost:2772/applications/{application_name}/environments/{environment_name}/configurations/{config_profile_name}",
#                         headers={"Entity-Id": entity_id})
# the agent runs a local HTTP server that serves configuration data
# make a GET request to the agent's local server to retrieve the configuration data
response = requests.get(f"http://localhost:2772/applications/{application_name}/environments/{environment_name}/configurations/{config_profile_name}")
config = response.content
```

------
#### [ JavaScript ]

```
// in this sample, we will retrieve configuration data from the AWS AppConfig Agent.
// the agent is a sidecar process that handles retrieving configuration data from AppConfig
// for you in a way that implements best practices like configuration caching.

// for more information about the agent, see
// [How to use AWS AppConfig Agent](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use.html)

const application_name = "MyDemoApp";
const environment_name = "MyEnvironment";
const config_profile_name = "MyConfigProfile";

// the agent runs a local HTTP server that serves configuration data
// make a GET request to the agent's local server to retrieve the configuration data
const url = `http://localhost:2772/applications/${application_name}/environments/${environment_name}/configurations/${config_profile_name}`;
// To enable entity-based deployments, add the Entity-Id header to the request:
// const response = await fetch(url, { headers: { "Entity-Id": entityId } });
const response = await fetch(url);
const config = await response.text(); // (use `await response.json()` if your config is json)
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
