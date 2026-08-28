---
source_url: https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/update-dashboards.html
---

# Update Dashboards
<a name="update-dashboards"></a>

## Update Dashboards
<a name="update-dashboards-2"></a>

**Important**
We recommend customers updating both cid-cmd tool and CID Cloud Formation stack to a version 4.2.3 or more recent.

We always improve Cloud Intelligence Dashboards by adding new actionable insights and recommendations. All new dashboard versions are announced in our [Changelog](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/tree/main/changes). You can find your current dashboard version on About tab of each of the dashboards.

To pull the latest version of the dashboard from the public template please use the following steps.

### Simple Update
<a name="simple-update"></a>

1. Open [CloudShell](https://console.aws.amazon.com/cloudshell/home) in the account where you have deployed the Cloud Intelligence Dashboards

1. Install cid-cmd tool. Run the following command and make sure you hit enter :

```
pip3 install --upgrade cid-cmd
```

1. Start update. Run the following command and choose the dashboard to update :

```
cid-cmd update
```

**Note**
After update Quick Sight datasets will be refreshed automatically. During the refresh process you may see "Dataset changed too much" error which should disappear once datasets are fully refreshed

### Recursive Update
<a name="recursive-update"></a>

#### Click here to see how resetting dashboards to the 'factory settings'
<a name="collapsible-section-id-update-dashboards-1"></a>

In some cases the update of underlying Quick Sight Datasets and views is required. This can also be useful to reset dashboards to factory settings if there is any issue. Please note that it might impact customizations you did on the dashboards. The tool will provide you an interactive prompt when it will detect the difference and you can accept the changes or keep existing.

```
cid-cmd update --force --recursive
```

### Update from CUDOS v4 to v5
<a name="update-from-cudos-v4-to-v5"></a>

If you are looking to update to CUDOS v5 from a previous CUDOS version, please refer to the guide in the [FAQs](faq.md)

### Update Demo
<a name="update-demo"></a>

[![AWS Videos](http://img.youtube.com/vi/ub7VWL2GJ84?rel=0/0.jpg)](http://www.youtube.com/watch?v=ub7VWL2GJ84?rel=0)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Intelligence Dashboards on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
