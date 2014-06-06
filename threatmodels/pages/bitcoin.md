title: Bitcoin
Application: Bitcoin
date: 2014-6-6
Trusted Parties: Minority of clients in the network
Untrusted Parties: Majority of clients in the network
Key Storage: Local
Convenience: Medium
Authentication: Chain of cryptographic signatures
Architecture: Distributed
tags:[Crypto-currency peer-to-peer]

# Intro
Bitcoin was the first and is the most widely used crypto-currency. It uses novel crpytographic constructions to prevent double spending and to fully de-centralize the network. It has resisted attack for sevral years in the wild and is generally considered very robust and secure.

# Trusted Parties
The trust comes from the fact that you belive that most of the computing power on the network is controlled by clients who are behaving honestly. This is a reasonable assumption because of the popularity of the crypto-curency and the ammount of attention that is paid to its status at any given moment. This is a virtue of the direct monetary value of the system. The incentive to protect the network is directly computable and that makes is more likeley that honest parties will expend resources to monitor it and protect it.

# Untrusted Parties
Because of the distributed nature of the Bitcoin network, and its requirement for proof-of-work, an attacker needs to control a significant portion of the computing power on the network in order for him/her to affect the networks normal operation. This means that any single node, or any sufficently small group of nodes should be considered "untrusted".

# Key Storage
Clients in the Bitcoin network are responsible for protecting their secret keys.

# Convenience
Bitcoin provides a unique service and in contrast to other services in the payment sector (ignoring copycats) it solves a whole host of problems, while providing unparalleled security and anonymity as well as robustness. The secret keys must still be properly managed by the user and therefore, Bitcoind only recieves a score of medium on the Convinience scale.

# Authentication
The authentication in the bitcoin network takes place in the block chain and is an ingenious way of protecting the public record of transactions. In order for a new block to get added to the chain, clients must solve a "hard" computation that includes a signature of the previous blocks. Changing a block requires eponentiual effort and changing an older block requires re-computing all the subsuquent blocks. This proof-of-work model means that cheating is made more expensive that it''s worth. This is true security.

# Architecture
There is no central authority in the bitcoin network, and it could even operate without a constant internet connection if it needed to.

