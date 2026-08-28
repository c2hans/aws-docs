---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_AdditionalInfoRequest.html
---

# AdditionalInfoRequest
<a name="API_taxSettings_AdditionalInfoRequest"></a>

Additional tax information associated with your tax registration number (TRN). Depending on the TRN for a specific country, you might need to specify this information when you set your TRN.

You can only specify one of the following parameters and the value can't be empty.

**Note**
The parameter that you specify must match the country for the TRN, if available. For example, if you set a TRN in Canada for specific provinces, you must also specify the `canadaAdditionalInfo` parameter.

## Contents
<a name="API_taxSettings_AdditionalInfoRequest_Contents"></a>

 ** belgiumAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-belgiumAdditionalInfo"></a>
Additional tax information to specify for a TRN in Belgium.
Type: [BelgiumAdditionalInfo](API_taxSettings_BelgiumAdditionalInfo.md) object
Required: No

 ** canadaAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-canadaAdditionalInfo"></a>
 Additional tax information associated with your TRN in Canada.
Type: [CanadaAdditionalInfo](API_taxSettings_CanadaAdditionalInfo.md) object
Required: No

 ** chileAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-chileAdditionalInfo"></a>
 Additional tax information to specify for a TRN in Chile.
Type: [ChileAdditionalInfo](API_taxSettings_ChileAdditionalInfo.md) object
Required: No

 ** egyptAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-egyptAdditionalInfo"></a>
Additional tax information to specify for a TRN in Egypt.
Type: [EgyptAdditionalInfo](API_taxSettings_EgyptAdditionalInfo.md) object
Required: No

 ** estoniaAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-estoniaAdditionalInfo"></a>
 Additional tax information to specify for a TRN in Estonia.
Type: [EstoniaAdditionalInfo](API_taxSettings_EstoniaAdditionalInfo.md) object
Required: No

 ** franceAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-franceAdditionalInfo"></a>
Additional tax information to specify for a TRN in France.
Type: [FranceAdditionalInfo](API_taxSettings_FranceAdditionalInfo.md) object
Required: No

 ** georgiaAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-georgiaAdditionalInfo"></a>
 Additional tax information to specify for a TRN in Georgia.
Type: [GeorgiaAdditionalInfo](API_taxSettings_GeorgiaAdditionalInfo.md) object
Required: No

 ** greeceAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-greeceAdditionalInfo"></a>
Additional tax information to specify for a TRN in Greece.
Type: [GreeceAdditionalInfo](API_taxSettings_GreeceAdditionalInfo.md) object
Required: No

 ** indonesiaAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-indonesiaAdditionalInfo"></a>

Type: [IndonesiaAdditionalInfo](API_taxSettings_IndonesiaAdditionalInfo.md) object
Required: No

 ** israelAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-israelAdditionalInfo"></a>
 Additional tax information to specify for a TRN in Israel.
Type: [IsraelAdditionalInfo](API_taxSettings_IsraelAdditionalInfo.md) object
Required: No

 ** italyAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-italyAdditionalInfo"></a>
 Additional tax information to specify for a TRN in Italy.
Type: [ItalyAdditionalInfo](API_taxSettings_ItalyAdditionalInfo.md) object
Required: No

 ** kenyaAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-kenyaAdditionalInfo"></a>
Additional tax information to specify for a TRN in Kenya.
Type: [KenyaAdditionalInfo](API_taxSettings_KenyaAdditionalInfo.md) object
Required: No

 ** malaysiaAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-malaysiaAdditionalInfo"></a>
 Additional tax information to specify for a TRN in Malaysia.
Type: [MalaysiaAdditionalInfo](API_taxSettings_MalaysiaAdditionalInfo.md) object
Required: No

 ** philippinesAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-philippinesAdditionalInfo"></a>
Additional tax information to specify for a TRN in the Philippines.
Type: [PhilippinesAdditionalInfo](API_taxSettings_PhilippinesAdditionalInfo.md) object
Required: No

 ** polandAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-polandAdditionalInfo"></a>
 Additional tax information associated with your TRN in Poland.
Type: [PolandAdditionalInfo](API_taxSettings_PolandAdditionalInfo.md) object
Required: No

 ** romaniaAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-romaniaAdditionalInfo"></a>
Additional tax information to specify for a TRN in Romania.
Type: [RomaniaAdditionalInfo](API_taxSettings_RomaniaAdditionalInfo.md) object
Required: No

 ** saudiArabiaAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-saudiArabiaAdditionalInfo"></a>
 Additional tax information associated with your TRN in Saudi Arabia.
Type: [SaudiArabiaAdditionalInfo](API_taxSettings_SaudiArabiaAdditionalInfo.md) object
Required: No

 ** southKoreaAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-southKoreaAdditionalInfo"></a>
Additional tax information to specify for a TRN in South Korea.
Type: [SouthKoreaAdditionalInfo](API_taxSettings_SouthKoreaAdditionalInfo.md) object
Required: No

 ** spainAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-spainAdditionalInfo"></a>
Additional tax information to specify for a TRN in Spain.
Type: [SpainAdditionalInfo](API_taxSettings_SpainAdditionalInfo.md) object
Required: No

 ** turkeyAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-turkeyAdditionalInfo"></a>
Additional tax information to specify for a TRN in Turkey.
Type: [TurkeyAdditionalInfo](API_taxSettings_TurkeyAdditionalInfo.md) object
Required: No

 ** ukraineAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-ukraineAdditionalInfo"></a>
 Additional tax information associated with your TRN in Ukraine.
Type: [UkraineAdditionalInfo](API_taxSettings_UkraineAdditionalInfo.md) object
Required: No

 ** uzbekistanAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-uzbekistanAdditionalInfo"></a>
 Additional tax information to specify for a TRN in Uzbekistan.
Type: [UzbekistanAdditionalInfo](API_taxSettings_UzbekistanAdditionalInfo.md) object
Required: No

 ** vietnamAdditionalInfo **   <a name="awscostmanagement-Type-taxSettings_AdditionalInfoRequest-vietnamAdditionalInfo"></a>
Additional tax information to specify for a TRN in Vietnam.
Type: [VietnamAdditionalInfo](API_taxSettings_VietnamAdditionalInfo.md) object
Required: No

## See Also
<a name="API_taxSettings_AdditionalInfoRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/AdditionalInfoRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/AdditionalInfoRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/AdditionalInfoRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
