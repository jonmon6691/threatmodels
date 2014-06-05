title: PGP
Application: PGP
date: 2014-06-03
Trusted Parties: Local Machine
Untrusted Parties: Any intermediary
Key Storage: Local
Convenience: Low
Authentication: Web of Trust
Architecture: federated
tags: [email]

# Intro

PGP is a method of end-to-end encryption for email. This means that the message
is encrypted by the sender and is not decrypted until it arrives on the
recipeients computer.

# Trusted Parties

Only the local machine of the sender and the recipient need to be trusted in
order for the security properties of PGP to be maintined.

# Untrusted Parties

Anyone handling a message encrypted with PGP does not need to be trusted.

# Key Storage

Keys are stored locally, or any arbitrary location of the user's choosing.

# Convenience

As mentioned below, the biggest sore spot of PGP is authentication. While the
web of trust is effective in small groups, it does not scale well and can be
compromised by taking advantage of less than rigorous particpants.

In addition to the authentication problem, nearly every implementation of PGP
requires manually copying and pasting encrypted messages into existing email
solutions.

Notably thunderbird with the enigmail extension makes PGP quite usable.
However, thunderbird is not actively developed. Further, this combination does
not solve the problem of a recipient needing to use PGP in order to recieve an
encrypted message.

For these reasons, the conveience of PGP is listed as low.

# Authentication

Authentication of PGP is done via the web of trust. This entails a key being
signed by another persons key after having verified their identity.

# Architecture

Since PGP is designed to encrypt email, the archiecture is considerd federated
since anyone can host an email server that can accept PGP messages.
