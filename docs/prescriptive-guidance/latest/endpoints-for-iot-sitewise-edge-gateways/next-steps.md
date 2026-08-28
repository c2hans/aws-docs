---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/endpoints-for-iot-sitewise-edge-gateways/next-steps.html
---

# Next steps
<a name="next-steps"></a>

Configure the allow list for the firewall in the internet perimeter zone to allow access to these endpoints. After you deploy the firewall access rules, you can use a utility, such as [GNU Netcat](https://netcat.sourceforge.net/), to test that the edge device can reach the endpoints in the AWS Cloud. The following is an example command that tests connectivity.

```
$ nc -z data.iotsitewise.us-east-1.amazonaws.com 443
Connection to data.iotsitewise.us-east-1.amazonaws.com port 443 [tcp/https] succeeded!
```

After you have successfully validated connectivity, deploy AWS IoT Greengrass V2 and the AWS IoT SiteWise Edge gateway. For more information, see [Setting up AWS IoT Greengrass V2](https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html) and [Using AWS IoT SiteWise gateways](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways-ggv2.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
