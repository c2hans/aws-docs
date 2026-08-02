---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_sesv2_code_examples.html
---

# Amazon SES API v2 examples using SDK for Rust
<a name="rust_sesv2_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with Amazon SES API v2.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)
+ [Scenarios](#scenarios)

## Actions
<a name="actions"></a>

### `CreateContact`
<a name="sesv2_CreateContact_rust_topic"></a>

The following code example shows how to use `CreateContact`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ses#code-examples).

```
async fn add_contact(client: &Client, list: &str, email: &str) -> Result<(), Error> {
    client
        .create_contact()
        .contact_list_name(list)
        .email_address(email)
        .send()
        .await?;

    println!("Created contact");

    Ok(())
}
```
+  For API details, see [CreateContact](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.create_contact) in *AWS SDK for Rust API reference*.

### `CreateContactList`
<a name="sesv2_CreateContactList_rust_topic"></a>

The following code example shows how to use `CreateContactList`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ses#code-examples).

```
async fn make_list(client: &Client, contact_list: &str) -> Result<(), Error> {
    client
        .create_contact_list()
        .contact_list_name(contact_list)
        .send()
        .await?;

    println!("Created contact list.");

    Ok(())
}
```
+  For API details, see [CreateContactList](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.create_contact_list) in *AWS SDK for Rust API reference*.

### `CreateEmailIdentity`
<a name="sesv2_CreateEmailIdentity_rust_topic"></a>

The following code example shows how to use `CreateEmailIdentity`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ses#code-examples).

```
        match self
            .client
            .create_email_identity()
            .email_identity(self.verified_email.clone())
            .send()
            .await
        {
            Ok(_) => writeln!(self.stdout, "Email identity created successfully.")?,
            Err(e) => match e.into_service_error() {
                CreateEmailIdentityError::AlreadyExistsException(_) => {
                    writeln!(
                        self.stdout,
                        "Email identity already exists, skipping creation."
                    )?;
                }
                e => return Err(anyhow!("Error creating email identity: {}", e)),
            },
        }
```
+  For API details, see [CreateEmailIdentity](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.create_email_identity) in *AWS SDK for Rust API reference*.

### `CreateEmailTemplate`
<a name="sesv2_CreateEmailTemplate_rust_topic"></a>

The following code example shows how to use `CreateEmailTemplate`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ses#code-examples).

```
        let template_html =
            std::fs::read_to_string("../resources/newsletter/coupon-newsletter.html")
                .unwrap_or_else(|_| "Missing coupon-newsletter.html".to_string());
        let template_text =
            std::fs::read_to_string("../resources/newsletter/coupon-newsletter.txt")
                .unwrap_or_else(|_| "Missing coupon-newsletter.txt".to_string());

        // Create the email template
        let template_content = EmailTemplateContent::builder()
            .subject("Weekly Coupons Newsletter")
            .html(template_html)
            .text(template_text)
            .build();

        match self
            .client
            .create_email_template()
            .template_name(TEMPLATE_NAME)
            .template_content(template_content)
            .send()
            .await
        {
            Ok(_) => writeln!(self.stdout, "Email template created successfully.")?,
            Err(e) => match e.into_service_error() {
                CreateEmailTemplateError::AlreadyExistsException(_) => {
                    writeln!(
                        self.stdout,
                        "Email template already exists, skipping creation."
                    )?;
                }
                e => return Err(anyhow!("Error creating email template: {}", e)),
            },
        }
```
+  For API details, see [CreateEmailTemplate](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.create_email_template) in *AWS SDK for Rust API reference*.

### `DeleteContactList`
<a name="sesv2_DeleteContactList_rust_topic"></a>

The following code example shows how to use `DeleteContactList`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ses#code-examples).

```
        match self
            .client
            .delete_contact_list()
            .contact_list_name(CONTACT_LIST_NAME)
            .send()
            .await
        {
            Ok(_) => writeln!(self.stdout, "Contact list deleted successfully.")?,
            Err(e) => return Err(anyhow!("Error deleting contact list: {e}")),
        }
```
+  For API details, see [DeleteContactList](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.delete_contact_list) in *AWS SDK for Rust API reference*.

### `DeleteEmailIdentity`
<a name="sesv2_DeleteEmailIdentity_rust_topic"></a>

The following code example shows how to use `DeleteEmailIdentity`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ses#code-examples).

```
            match self
                .client
                .delete_email_identity()
                .email_identity(self.verified_email.clone())
                .send()
                .await
            {
                Ok(_) => writeln!(self.stdout, "Email identity deleted successfully.")?,
                Err(e) => {
                    return Err(anyhow!("Error deleting email identity: {}", e));
                }
            }
```
+  For API details, see [DeleteEmailIdentity](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.delete_email_identity) in *AWS SDK for Rust API reference*.

### `DeleteEmailTemplate`
<a name="sesv2_DeleteEmailTemplate_rust_topic"></a>

The following code example shows how to use `DeleteEmailTemplate`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ses#code-examples).

```
        match self
            .client
            .delete_email_template()
            .template_name(TEMPLATE_NAME)
            .send()
            .await
        {
            Ok(_) => writeln!(self.stdout, "Email template deleted successfully.")?,
            Err(e) => {
                return Err(anyhow!("Error deleting email template: {e}"));
            }
        }
```
+  For API details, see [DeleteEmailTemplate](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.delete_email_template) in *AWS SDK for Rust API reference*.

### `GetEmailIdentity`
<a name="sesv2_GetEmailIdentity_rust_topic"></a>

The following code example shows how to use `GetEmailIdentity`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ses#code-examples).
Determines whether an email address has been verified.

```
async fn is_verified(client: &Client, email: &str) -> Result<(), Error> {
    let resp = client
        .get_email_identity()
        .email_identity(email)
        .send()
        .await?;

    if resp.verified_for_sending_status() {
        println!("The address is verified");
    } else {
        println!("The address is not verified");
    }

    Ok(())
}
```
+  For API details, see [GetEmailIdentity](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.get_email_identity) in *AWS SDK for Rust API reference*.

### `ListContactLists`
<a name="sesv2_ListContactLists_rust_topic"></a>

The following code example shows how to use `ListContactLists`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ses#code-examples).

```
async fn show_lists(client: &Client) -> Result<(), Error> {
    let resp = client.list_contact_lists().send().await?;

    println!("Contact lists:");

    for list in resp.contact_lists() {
        println!("  {}", list.contact_list_name().unwrap_or_default());
    }

    Ok(())
}
```
+  For API details, see [ListContactLists](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.list_contact_lists) in *AWS SDK for Rust API reference*.

### `ListContacts`
<a name="sesv2_ListContacts_rust_topic"></a>

The following code example shows how to use `ListContacts`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ses#code-examples).

```
async fn show_contacts(client: &Client, list: &str) -> Result<(), Error> {
    let resp = client
        .list_contacts()
        .contact_list_name(list)
        .send()
        .await?;

    println!("Contacts:");

    for contact in resp.contacts() {
        println!("  {}", contact.email_address().unwrap_or_default());
    }

    Ok(())
}
```
+  For API details, see [ListContacts](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.list_contacts) in *AWS SDK for Rust API reference*.

### `SendEmail`
<a name="sesv2_SendEmail_rust_topic"></a>

The following code example shows how to use `SendEmail`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ses#code-examples).
Sends a message to all members of the contact list.

```
async fn send_message(
    client: &Client,
    list: &str,
    from: &str,
    subject: &str,
    message: &str,
) -> Result<(), Error> {
    // Get list of email addresses from contact list.
    let resp = client
        .list_contacts()
        .contact_list_name(list)
        .send()
        .await?;

    let contacts = resp.contacts();

    let cs: Vec<String> = contacts
        .iter()
        .map(|i| i.email_address().unwrap_or_default().to_string())
        .collect();

    let mut dest: Destination = Destination::builder().build();
    dest.to_addresses = Some(cs);
    let subject_content = Content::builder()
        .data(subject)
        .charset("UTF-8")
        .build()
        .expect("building Content");
    let body_content = Content::builder()
        .data(message)
        .charset("UTF-8")
        .build()
        .expect("building Content");
    let body = Body::builder().text(body_content).build();

    let msg = Message::builder()
        .subject(subject_content)
        .body(body)
        .build();

    let email_content = EmailContent::builder().simple(msg).build();

    client
        .send_email()
        .from_email_address(from)
        .destination(dest)
        .content(email_content)
        .send()
        .await?;

    println!("Email sent to list");

    Ok(())
}
```
Sends a message to all members of the contact list using a template.

```
            let coupons = std::fs::read_to_string("../resources/newsletter/sample_coupons.json")
                .unwrap_or_else(|_| r#"{"coupons":[]}"#.to_string());
            let email_content = EmailContent::builder()
                .template(
                    Template::builder()
                        .template_name(TEMPLATE_NAME)
                        .template_data(coupons)
                        .build(),
                )
                .build();

            match self
                .client
                .send_email()
                .from_email_address(self.verified_email.clone())
                .destination(Destination::builder().to_addresses(email.clone()).build())
                .content(email_content)
                .list_management_options(
                    ListManagementOptions::builder()
                        .contact_list_name(CONTACT_LIST_NAME)
                        .build()?,
                )
                .send()
                .await
            {
                Ok(output) => {
                    if let Some(message_id) = output.message_id {
                        writeln!(
                            self.stdout,
                            "Newsletter sent to {} with message ID {}",
                            email, message_id
                        )?;
                    } else {
                        writeln!(self.stdout, "Newsletter sent to {}", email)?;
                    }
                }
                Err(e) => return Err(anyhow!("Error sending newsletter to {}: {}", email, e)),
            }
```
+  For API details, see [SendEmail](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.send_email) in *AWS SDK for Rust API reference*.

## Scenarios
<a name="scenarios"></a>

### Newsletter scenario
<a name="sesv2_NewsletterWorkflow_rust_topic"></a>

The following code example shows how to run the Amazon SES API v2 newsletter scenario.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ses#code-examples).

```
        match self
            .client
            .create_contact_list()
            .contact_list_name(CONTACT_LIST_NAME)
            .send()
            .await
        {
            Ok(_) => writeln!(self.stdout, "Contact list created successfully.")?,
            Err(e) => match e.into_service_error() {
                CreateContactListError::AlreadyExistsException(_) => {
                    writeln!(
                        self.stdout,
                        "Contact list already exists, skipping creation."
                    )?;
                }
                e => return Err(anyhow!("Error creating contact list: {}", e)),
            },
        }

            match self
                .client
                .create_contact()
                .contact_list_name(CONTACT_LIST_NAME)
                .email_address(email.clone())
                .send()
                .await
            {
                Ok(_) => writeln!(self.stdout, "Contact created for {}", email)?,
                Err(e) => match e.into_service_error() {
                    CreateContactError::AlreadyExistsException(_) => writeln!(
                        self.stdout,
                        "Contact already exists for {}, skipping creation.",
                        email
                    )?,
                    e => return Err(anyhow!("Error creating contact for {}: {}", email, e)),
                },
            }

        let contacts: Vec<Contact> = match self
            .client
            .list_contacts()
            .contact_list_name(CONTACT_LIST_NAME)
            .send()
            .await
        {
            Ok(list_contacts_output) => {
                list_contacts_output.contacts.unwrap().into_iter().collect()
            }
            Err(e) => {
                return Err(anyhow!(
                    "Error retrieving contact list {}: {}",
                    CONTACT_LIST_NAME,
                    e
                ))
            }
        };

            let coupons = std::fs::read_to_string("../resources/newsletter/sample_coupons.json")
                .unwrap_or_else(|_| r#"{"coupons":[]}"#.to_string());
            let email_content = EmailContent::builder()
                .template(
                    Template::builder()
                        .template_name(TEMPLATE_NAME)
                        .template_data(coupons)
                        .build(),
                )
                .build();

            match self
                .client
                .send_email()
                .from_email_address(self.verified_email.clone())
                .destination(Destination::builder().to_addresses(email.clone()).build())
                .content(email_content)
                .list_management_options(
                    ListManagementOptions::builder()
                        .contact_list_name(CONTACT_LIST_NAME)
                        .build()?,
                )
                .send()
                .await
            {
                Ok(output) => {
                    if let Some(message_id) = output.message_id {
                        writeln!(
                            self.stdout,
                            "Newsletter sent to {} with message ID {}",
                            email, message_id
                        )?;
                    } else {
                        writeln!(self.stdout, "Newsletter sent to {}", email)?;
                    }
                }
                Err(e) => return Err(anyhow!("Error sending newsletter to {}: {}", email, e)),
            }

        match self
            .client
            .create_email_identity()
            .email_identity(self.verified_email.clone())
            .send()
            .await
        {
            Ok(_) => writeln!(self.stdout, "Email identity created successfully.")?,
            Err(e) => match e.into_service_error() {
                CreateEmailIdentityError::AlreadyExistsException(_) => {
                    writeln!(
                        self.stdout,
                        "Email identity already exists, skipping creation."
                    )?;
                }
                e => return Err(anyhow!("Error creating email identity: {}", e)),
            },
        }

        let template_html =
            std::fs::read_to_string("../resources/newsletter/coupon-newsletter.html")
                .unwrap_or_else(|_| "Missing coupon-newsletter.html".to_string());
        let template_text =
            std::fs::read_to_string("../resources/newsletter/coupon-newsletter.txt")
                .unwrap_or_else(|_| "Missing coupon-newsletter.txt".to_string());

        // Create the email template
        let template_content = EmailTemplateContent::builder()
            .subject("Weekly Coupons Newsletter")
            .html(template_html)
            .text(template_text)
            .build();

        match self
            .client
            .create_email_template()
            .template_name(TEMPLATE_NAME)
            .template_content(template_content)
            .send()
            .await
        {
            Ok(_) => writeln!(self.stdout, "Email template created successfully.")?,
            Err(e) => match e.into_service_error() {
                CreateEmailTemplateError::AlreadyExistsException(_) => {
                    writeln!(
                        self.stdout,
                        "Email template already exists, skipping creation."
                    )?;
                }
                e => return Err(anyhow!("Error creating email template: {}", e)),
            },
        }

        match self
            .client
            .delete_contact_list()
            .contact_list_name(CONTACT_LIST_NAME)
            .send()
            .await
        {
            Ok(_) => writeln!(self.stdout, "Contact list deleted successfully.")?,
            Err(e) => return Err(anyhow!("Error deleting contact list: {e}")),
        }

            match self
                .client
                .delete_email_identity()
                .email_identity(self.verified_email.clone())
                .send()
                .await
            {
                Ok(_) => writeln!(self.stdout, "Email identity deleted successfully.")?,
                Err(e) => {
                    return Err(anyhow!("Error deleting email identity: {}", e));
                }
            }

        match self
            .client
            .delete_email_template()
            .template_name(TEMPLATE_NAME)
            .send()
            .await
        {
            Ok(_) => writeln!(self.stdout, "Email template deleted successfully.")?,
            Err(e) => {
                return Err(anyhow!("Error deleting email template: {e}"));
            }
        }
```
+ For API details, see the following topics in *AWS SDK for Rust API reference*.
  + [CreateContact](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.create_contact)
  + [CreateContactList](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.create_contact_list)
  + [CreateEmailIdentity](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.create_email_identity)
  + [CreateEmailTemplate](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.create_email_template)
  + [DeleteContactList](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.delete_contact_list)
  + [DeleteEmailIdentity](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.delete_email_identity)
  + [DeleteEmailTemplate](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.delete_email_template)
  + [ListContacts](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.list_contacts)
  + [SendEmail.simple](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.send_email.simple)
  + [SendEmail.template](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.send_email.template)
