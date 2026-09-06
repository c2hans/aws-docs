---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-adspersonalizationconcurrency.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration AdsPersonalizationConcurrency
<a name="aws-properties-mediatailor-playbackconfiguration-adspersonalizationconcurrency"></a>

The concurrency settings for ad decision server interactions during ad personalization.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-adspersonalizationconcurrency-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-adspersonalizationconcurrency-syntax.json"></a>

```
{
  "[EnableVodVastParallelization](#cfn-mediatailor-playbackconfiguration-adspersonalizationconcurrency-enablevodvastparallelization)" : {{Boolean}},
  "[MaxConcurrentAdsRequests](#cfn-mediatailor-playbackconfiguration-adspersonalizationconcurrency-maxconcurrentadsrequests)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-adspersonalizationconcurrency-syntax.yaml"></a>

```
  [EnableVodVastParallelization](#cfn-mediatailor-playbackconfiguration-adspersonalizationconcurrency-enablevodvastparallelization): {{Boolean}}
  [MaxConcurrentAdsRequests](#cfn-mediatailor-playbackconfiguration-adspersonalizationconcurrency-maxconcurrentadsrequests): {{Integer}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-adspersonalizationconcurrency-properties"></a>

`EnableVodVastParallelization`  <a name="cfn-mediatailor-playbackconfiguration-adspersonalizationconcurrency-enablevodvastparallelization"></a>
Enables parallel processing of ad decision server requests in VOD workflows when the ADS returns VAST responses. The default is false.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxConcurrentAdsRequests`  <a name="cfn-mediatailor-playbackconfiguration-adspersonalizationconcurrency-maxconcurrentadsrequests"></a>
The maximum number of simultaneous requests that MediaTailor makes to the ad decision server per manifest request. The default is 1.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
