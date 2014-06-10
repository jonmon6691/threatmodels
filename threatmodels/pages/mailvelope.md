title: Mailvelope
Application: Mailvelope
date: 2014-06-10
Trusted Parties: Local Machine
Untrusted Parties: Any intermediary
Key Storage: HTML5 localStorage
Convenience: Low
Authentication: Web of Trust
Architecture: Federated
tags:[email, browser-extension]

# Intro

Mailvelope is a browser extension for Google Chrome and Mozilla Firefox.
Fundamentally, it provides a user interface for using OpenPGP on any website
that allows user input. Users open the browser extension by clicking an icon
within an input form on any whitelisted page. Within that interface the message
and public keys are specified. After encrypting a message, users copy and paste
the ciphertext into the input form. After receiving an encrypted message users
can use Mailvelope to decrypt ciphertext.

# Trusted Parties

The local machine must be trusted. Mailvelope requires that the browser is
completely trusted and that no hostile browser extensions are installed. The
open source implementation of OpenPGP in javascript, OpenPGP.js, must also be
trusted.

# Untrusted Parties

Mailvelope allows any website to be completely untrusted since user input is
encrypted before it is entered. Any intermediary handling the ciphertext need
not be trusted.

# Key Storage

Public and private keys are stored in HTML5 localStorage. This storage is in
theory remotely accessible, but is protected by the same origin policy. If
Mailvelope is vulnerable to a CSRF attack, the keys could be revealed to a
third party.

# Convenience

Mailvelope brings PGP, and all of the inconvenience that accompanies it, to the
web. While Mailvelope is much easier to use than a PGP command line utility, it
still requires knowing your recipients public key in advance. The problems of
authentication are not mitigated.

The user interaction of copying and pasting ciphertext in and out of Mailvelope
is well designed, but fundamentally awkward. This interaction could be a
security hole if incorrectly handled by the user. For example, if a user types
their message into gmail before copying it into Mailvelope to be encrypted,
then gmail has access to the plaintext before it is encrypted.

# Authentication

Mailvelope does not provided any means of authentication beyond what standard
OpenPGP offers.

# Architecture

Since anyone can run Mailvelope, the architecture of Mailvelope is considered
federated.
