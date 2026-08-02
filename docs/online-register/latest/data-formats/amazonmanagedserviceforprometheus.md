---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazonmanagedserviceforprometheus.html
---

# Data retrieval APIs for Amazon Managed Service for Prometheus
<a name="amazonmanagedserviceforprometheus"></a>

Amazon Managed Service for Prometheus provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="aps-DescribeAlertManagerDefinition"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeAlertManagerDefinition.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeAlertManagerDefinition.html) | Describe an alert manager definition | Read |
| <a name="aps-DescribeAnomalyDetector"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeAnomalyDetector.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeAnomalyDetector.html) | Describe an anomaly detector | Read |
| <a name="aps-DescribeLoggingConfiguration"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeLoggingConfiguration.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeLoggingConfiguration.html) | Describe a logging configuration | Read |
| <a name="aps-DescribeQueryLoggingConfiguration"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeQueryLoggingConfiguration.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeQueryLoggingConfiguration.html) | Describe a query logging configuration | Read |
| <a name="aps-DescribeResourcePolicy"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeResourcePolicy.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeResourcePolicy.html) | Describe workspace resource policy | Read |
| <a name="aps-DescribeRuleGroupsNamespace"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeRuleGroupsNamespace.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeRuleGroupsNamespace.html) | Describe a rule groups namespace | Read |
| <a name="aps-DescribeScraper"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeScraper.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeScraper.html) | Describe a scraper | Read |
| <a name="aps-DescribeScraperLoggingConfiguration"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeScraperLoggingConfiguration.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeScraperLoggingConfiguration.html) | Describe a scraper logging configuration | Read |
| <a name="aps-DescribeWorkspace"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeWorkspace.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeWorkspace.html) | Describe a workspace | Read |
| <a name="aps-DescribeWorkspaceConfiguration"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeWorkspaceConfiguration.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeWorkspaceConfiguration.html) | Describe workspace configuration | Read |
| <a name="aps-GetAlertManagerSilence"></a>[https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetAlertManagerSilence.html](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetAlertManagerSilence.html) | Get a silence | Read |
| <a name="aps-GetAlertManagerStatus"></a>[https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetAlertManagerStatus.html](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetAlertManagerStatus.html) | Get current status of an alertmanager | Read |
| <a name="aps-GetDefaultScraperConfiguration"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_GetDefaultScraperConfiguration.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_GetDefaultScraperConfiguration.html) | Get default scraper configuration | Read |
| <a name="aps-GetLabels"></a>[https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetLabels.html](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetLabels.html) | Retrieve AMP workspace labels | Read |
| <a name="aps-GetMetricMetadata"></a>[https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetMetricMetadata.html](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetMetricMetadata.html) | Retrieve the metadata for AMP workspace metrics | Read |
| <a name="aps-GetSeries"></a>[https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetSeries.html](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-GetSeries.html) | Retrieve AMP workspace time series data | Read |
| <a name="aps-ListAlertManagerAlertGroups"></a>[https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerAlertGroups.html](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerAlertGroups.html) | List groups | Read |
| <a name="aps-ListAlertManagerAlerts"></a>[https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerAlerts.html](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerAlerts.html) | List alerts | Read |
| <a name="aps-ListAlertManagerReceivers"></a>[https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerReceivers.html](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerReceivers.html) | List receivers | Read |
| <a name="aps-ListAlertManagerSilences"></a>[https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerSilences.html](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlertManagerSilences.html) | List silences | Read |
| <a name="aps-ListAlerts"></a>[https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlerts.html](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListAlerts.html) | List active alerts | Read |
| <a name="aps-ListAnomalyDetectors"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListAnomalyDetectors.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListAnomalyDetectors.html) | List anomaly detectors | List |
| <a name="aps-ListRuleGroupsNamespaces"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListRuleGroupsNamespaces.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListRuleGroupsNamespaces.html) | List rule groups namespaces | List |
| <a name="aps-ListRules"></a>[https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListRules.html](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-ListRules.html) | List alerting and recording rules | Read |
| <a name="aps-ListScrapers"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListScrapers.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListScrapers.html) | List scrapers | List |
| <a name="aps-ListTagsForResource"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListTagsForResource.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListTagsForResource.html) | List tags on an AMP resource | Read |
| <a name="aps-ListWorkspaces"></a>[https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListWorkspaces.html](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListWorkspaces.html) | List workspaces | List |
| <a name="aps-PreviewAnomalyDetector"></a>[https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-PreviewAnomalyDetector.html](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-PreviewAnomalyDetector.html) | Preview anomaly detection on AMP workspace metrics | Read |
| <a name="aps-QueryMetrics"></a>[https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-QueryMetrics.html](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-QueryMetrics.html) | Run a query on AMP workspace metrics | Read |
