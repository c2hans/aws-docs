---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_Types.html
---

# Data Types
<a name="API_Types"></a>

The Payment Cryptography Data Plane API contains several data types that various actions use. This section describes each data type in detail.

**Note**
The order of each element in a data type structure is not guaranteed. Applications should not assume a particular order.

The following data types are supported:
+  [AmexAttributes](API_AmexAttributes.md)
+  [AmexCardSecurityCodeVersion1](API_AmexCardSecurityCodeVersion1.md)
+  [AmexCardSecurityCodeVersion2](API_AmexCardSecurityCodeVersion2.md)
+  [As2805KekValidationType](API_As2805KekValidationType.md)
+  [As2805PekDerivationAttributes](API_As2805PekDerivationAttributes.md)
+  [AsymmetricEncryptionAttributes](API_AsymmetricEncryptionAttributes.md)
+  [CardGenerationAttributes](API_CardGenerationAttributes.md)
+  [CardHolderVerificationValue](API_CardHolderVerificationValue.md)
+  [CardVerificationAttributes](API_CardVerificationAttributes.md)
+  [CardVerificationValue1](API_CardVerificationValue1.md)
+  [CardVerificationValue2](API_CardVerificationValue2.md)
+  [CryptogramAuthResponse](API_CryptogramAuthResponse.md)
+  [CryptogramVerificationArpcMethod1](API_CryptogramVerificationArpcMethod1.md)
+  [CryptogramVerificationArpcMethod2](API_CryptogramVerificationArpcMethod2.md)
+  [CurrentPinAttributes](API_CurrentPinAttributes.md)
+  [DerivationMethodAttributes](API_DerivationMethodAttributes.md)
+  [DiffieHellmanDerivationData](API_DiffieHellmanDerivationData.md)
+  [DiscoverDynamicCardVerificationCode](API_DiscoverDynamicCardVerificationCode.md)
+  [DukptAttributes](API_DukptAttributes.md)
+  [DukptDerivationAttributes](API_DukptDerivationAttributes.md)
+  [DukptEncryptionAttributes](API_DukptEncryptionAttributes.md)
+  [DynamicCardVerificationCode](API_DynamicCardVerificationCode.md)
+  [DynamicCardVerificationValue](API_DynamicCardVerificationValue.md)
+  [EcdhDerivationAttributes](API_EcdhDerivationAttributes.md)
+  [Emv2000Attributes](API_Emv2000Attributes.md)
+  [EmvCommonAttributes](API_EmvCommonAttributes.md)
+  [EmvEncryptionAttributes](API_EmvEncryptionAttributes.md)
+  [EncryptionDecryptionAttributes](API_EncryptionDecryptionAttributes.md)
+  [Ibm3624NaturalPin](API_Ibm3624NaturalPin.md)
+  [Ibm3624PinFromOffset](API_Ibm3624PinFromOffset.md)
+  [Ibm3624PinOffset](API_Ibm3624PinOffset.md)
+  [Ibm3624PinVerification](API_Ibm3624PinVerification.md)
+  [Ibm3624RandomPin](API_Ibm3624RandomPin.md)
+  [IncomingDiffieHellmanTr31KeyBlock](API_IncomingDiffieHellmanTr31KeyBlock.md)
+  [IncomingKeyMaterial](API_IncomingKeyMaterial.md)
+  [KekValidationRequest](API_KekValidationRequest.md)
+  [KekValidationResponse](API_KekValidationResponse.md)
+  [MacAlgorithmDukpt](API_MacAlgorithmDukpt.md)
+  [MacAlgorithmEmv](API_MacAlgorithmEmv.md)
+  [MacAttributes](API_MacAttributes.md)
+  [MasterCardAttributes](API_MasterCardAttributes.md)
+  [OutgoingKeyMaterial](API_OutgoingKeyMaterial.md)
+  [OutgoingTr31KeyBlock](API_OutgoingTr31KeyBlock.md)
+  [PinData](API_PinData.md)
+  [PinGenerationAttributes](API_PinGenerationAttributes.md)
+  [PinVerificationAttributes](API_PinVerificationAttributes.md)
+  [ReEncryptionAttributes](API_ReEncryptionAttributes.md)
+  [SessionKeyAmex](API_SessionKeyAmex.md)
+  [SessionKeyDerivation](API_SessionKeyDerivation.md)
+  [SessionKeyDerivationValue](API_SessionKeyDerivationValue.md)
+  [SessionKeyEmv2000](API_SessionKeyEmv2000.md)
+  [SessionKeyEmvCommon](API_SessionKeyEmvCommon.md)
+  [SessionKeyMastercard](API_SessionKeyMastercard.md)
+  [SessionKeyVisa](API_SessionKeyVisa.md)
+  [SymmetricEncryptionAttributes](API_SymmetricEncryptionAttributes.md)
+  [TranslationIsoFormats](API_TranslationIsoFormats.md)
+  [TranslationPinDataAs2805Format0](API_TranslationPinDataAs2805Format0.md)
+  [TranslationPinDataIsoFormat034](API_TranslationPinDataIsoFormat034.md)
+  [TranslationPinDataIsoFormat1](API_TranslationPinDataIsoFormat1.md)
+  [ValidationExceptionField](API_ValidationExceptionField.md)
+  [VisaAmexDerivationOutputs](API_VisaAmexDerivationOutputs.md)
+  [VisaAttributes](API_VisaAttributes.md)
+  [VisaPin](API_VisaPin.md)
+  [VisaPinVerification](API_VisaPinVerification.md)
+  [VisaPinVerificationValue](API_VisaPinVerificationValue.md)
+  [WrappedKey](API_WrappedKey.md)
+  [WrappedKeyMaterial](API_WrappedKeyMaterial.md)
+  [WrappedWorkingKey](API_WrappedWorkingKey.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
