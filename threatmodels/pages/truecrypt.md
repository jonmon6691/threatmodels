title: Truecrypt
Application: Truecrypt
date: 2014-6-13
Trusted Parties: Local Machine, Application Distributor
Untrusted Parties: N/A
Key Storage: Passphrase
Convenience: High
Authentication: None
Architecture: Local encryption service
tags:[Lock-box Full-disk-encryption encryption]

# Intro
Truecrypt is a program that you can install on your computer that allows you
to create encrypted volumes of any pre-set size. It has been a staple in the
security software ecosystem until recently when a mysterious security warning
from its creators hints at a possible unfixed security compromise in its
source code. Using Truecrypt is NOT recommended because of this.

# Trusted Parties
Normally for a service like Truecrypt, we would only need to trust the local
machine that was running the software and we would assume that the software was
performing as intended. However, the anonymous maintainers of the Truecrypt
project withdrew support for it, posted a warning that the software should no
longer be considered secure, and released a special version to aid in
transferring old encrypted archives to other services. All of this came without
any explanation from the developer other than the possibility of "Unfixed
Security Issues". This brings up the difficult notion that all regardless of
the threat model, all services require you to trust the developer. Even in open
source projects like Truecrypt, a majority of the users will download
pre-compiled binaries which may or may not reflect the available source code.

# Untrusted Parties
Truecrypt is used locally and does not require parties other than those listed
above.

# Key Storage
Truecrypt volumes can be encrypted with a pass phrase, a key file, or both.
These must be managed by the user of the program and would be considered local
Key storage.

# Convenience
The Truecrypt program makes it very easy to store files in an encrypted blob 
by mounting the encrypted file as a virtual hard disk and seamlessly encrypting
everything written to the virtual disk. This makes the encryption process
transparent to any program using the drive and is a huge bonus to convenience.

# Authentication
Trucrypt uses symmetric key cryptography and does not support any forms of
authentication. If the correct pass phrase and or key files are used, the
volume can be decrypted.

# Architecture
Since Truecrypt does not involve the internet, or any other networking service,
is does not fall under the three major security service categories: Silo,
Federated, or peer-to-peer. Instead, it is simply considered to be a local
encryption service.
