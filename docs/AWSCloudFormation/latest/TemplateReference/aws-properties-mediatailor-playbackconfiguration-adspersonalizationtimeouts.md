---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-adspersonalizationtimeouts.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration AdsPersonalizationTimeouts
<a name="aws-properties-mediatailor-playbackconfiguration-adspersonalizationtimeouts"></a>

The timeout settings for ad decision server interactions during ad personalization.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-adspersonalizationtimeouts-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-adspersonalizationtimeouts-syntax.json"></a>

```
{
  "[AdsRequestTimeoutMilliseconds](#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-adsrequesttimeoutmilliseconds)" : {{Integer}},
  "[LiveMaximumAdsPersonalizationTimeMilliseconds](#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-livemaximumadspersonalizationtimemilliseconds)" : {{Integer}},
  "[PrefetchAdsRequestTimeoutMilliseconds](#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-prefetchadsrequesttimeoutmilliseconds)" : {{Integer}},
  "[PrefetchMaximumAdsPersonalizationTimeMilliseconds](#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-prefetchmaximumadspersonalizationtimemilliseconds)" : {{Integer}},
  "[VodMaximumAdsPersonalizationTimeMilliseconds](#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-vodmaximumadspersonalizationtimemilliseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-adspersonalizationtimeouts-syntax.yaml"></a>

```
  [AdsRequestTimeoutMilliseconds](#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-adsrequesttimeoutmilliseconds): {{Integer}}
  [LiveMaximumAdsPersonalizationTimeMilliseconds](#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-livemaximumadspersonalizationtimemilliseconds): {{Integer}}
  [PrefetchAdsRequestTimeoutMilliseconds](#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-prefetchadsrequesttimeoutmilliseconds): {{Integer}}
  [PrefetchMaximumAdsPersonalizationTimeMilliseconds](#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-prefetchmaximumadspersonalizationtimemilliseconds): {{Integer}}
  [VodMaximumAdsPersonalizationTimeMilliseconds](#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-vodmaximumadspersonalizationtimemilliseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-adspersonalizationtimeouts-properties"></a>

`AdsRequestTimeoutMilliseconds`  <a name="cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-adsrequesttimeoutmilliseconds"></a>
The maximum time, in milliseconds, that MediaTailor waits for a single ad decision server response during live or VOD playback. The default is 3000.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LiveMaximumAdsPersonalizationTimeMilliseconds`  <a name="cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-livemaximumadspersonalizationtimemilliseconds"></a>
The maximum total time, in milliseconds, that MediaTailor spends on ad decision server activity for live manifests, including making requests, waiting for responses, and following VAST wrapper redirects. The default is 10000.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrefetchAdsRequestTimeoutMilliseconds`  <a name="cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-prefetchadsrequesttimeoutmilliseconds"></a>
The maximum time, in milliseconds, that MediaTailor waits for a single ad decision server response during prefetch retrieval. If not set, the value of AdsRequestTimeoutMilliseconds is used.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrefetchMaximumAdsPersonalizationTimeMilliseconds`  <a name="cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-prefetchmaximumadspersonalizationtimemilliseconds"></a>
The maximum total time, in milliseconds, that MediaTailor spends on ad decision server activity during prefetch retrieval, including making requests, waiting for responses, and following VAST wrapper redirects.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VodMaximumAdsPersonalizationTimeMilliseconds`  <a name="cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-vodmaximumadspersonalizationtimemilliseconds"></a>
The maximum total time, in milliseconds, that MediaTailor spends on ad decision server activity for VOD manifests, including making requests, waiting for responses, and following VAST wrapper redirects. The default is 10000.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
