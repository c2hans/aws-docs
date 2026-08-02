---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-banking-modernization-clm/strategy-onboarding-case.html
---

# The onboarding customer journey
<a name="strategy-onboarding-case"></a>

A modernized customer journey for opening an account should include the following features and capabilities:
+ The customer can access the onboarding service through an internet website, virtual assistant, or call center. The virtual assistant can be a text-oriented or speech-oriented chatbot, which can be integrated into a webpage or into a messaging application like Messenger or Telegram.
+ Virtual assistants can interact with customers by using predefined intents to understand the customer's needs and background. For example, the virtual assistant can ask clients to share their interests, share personal details to open an account, scan their ID and take a selfie, or confirm that they want to proceed with opening an account.
+ The chatbot will be multi-lingual.
+ Customers can interact with the chatbot using voice or text.
+ After you collect all the required information from the customer, then you can send the information to the bank to initiate the account opening process. The customer will receive an email notification confirming that the process started.
+ You can close the dialog after the account has been opened.
+ Avoid storing customer information in the cloud. This information must be transient and exist only during the customer engagement. After the account opening process is completed, you must delete the data and, if possible, provide some evidence of the deletion. Even if the dialog is interrupted, you must confirm that all personal data is deleted (no caching).
+ Avoid storing logs with personally identifiable information (PII).
+ Customers can be confident that no PII data is stored. If the services used are serverless, then no data or logs with personal data remain.
