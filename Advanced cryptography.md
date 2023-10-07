## Resources

- [coursera](https://www.coursera.org/learn/crypto/home/week/1)
- [cryptography-youtube](https://youtu.be/xEp0Fx-kZNM?si=E5uUil1hL6f_trX_)
- [java-crypto](https://youtu.be/UNZzilk8bo8?si=i-5BVII77PDl9_6I)
- [java-2](https://youtu.be/J1RmZZEkN0k?si=RrkJnETaO9szdDRG)


## Topics

- [x] **Introduction to Cryptography**
  - [ ] Overview of cryptography's history and significance
  - [ ] Basic principles of encryption and decryption
  - [ ] Symmetric vs. asymmetric encryption

- [x] **Symmetric-Key Encryption**
  - [ ] Study of symmetric encryption algorithms (e.g., DES, AES)
  - [ ] Mathematical foundations and operations
  - [ ] Block cipher modes of operation (e.g., ECB, CBC)
  - [ ] Padding schemes

- [ ] **Asymmetric Encryption**
  - [ ] In-depth exploration of asymmetric encryption algorithms (e.g., RSA)
  - [ ] Mathematical principles behind RSA
  - [ ] RSA key generation process
  - [ ] Implementation of RSA encryption and decryption

- [ ] **Merkle-Damgård Construction and Hash Functions**
  - [ ] Understanding cryptographic hash functions (e.g., SHA-256, SHA-3)
  - [ ] Properties of hash functions (preimage resistance, collision resistance, etc.)
  - [ ] Focus on Merkle-Damgård construction for building hash functions
  - [ ] Study of padding schemes (e.g., PKCS#7) in hash functions
  - [ ] Implementation of a simple hash function using Merkle-Damgård

- [ ] **MACs (Message Authentication Codes)**
  - [ ]  what is extensional forgery
  - [ ] Introduction to HMAC (Hash-based Message Authentication Code)
  - [ ] Non hash based macs (NMAC & CBC-MAC)

- [ ] **Public Key Infrastructure (PKI)**
  - [ ] Introduction to PKI and digital certificates
  - [ ] Role of certificate authorities (CAs)
  - [ ] Certificate issuance and validation processes
  - [ ] PKI in web browsers and applications

- [ ] **Authenticated encryption (tls,ssh,ipsec)**
  - [ ] What is authenticated encryption.
  - [ ] Study of the TLS protocol for secure internet communication
  - [ ] Key components of TLS (key exchange, encryption algorithms, handshake process)
  - [ ] Implementation of a simple client-server application using TLS
  - [ ] Study of cryptographic protocols beyond TLS (IPsec, SSH, etc.)

- [ ] **Cryptographic Attacks and Countermeasures**
  - [ ] Exploration of common cryptographic attacks (brute force, dictionary attacks, timing attacks)
  - [ ] Countermeasures (salting, key stretching, password hashing)

- [ ] **Cryptography Use Cases**
  - [ ] **File Systems Encryption**
    - [ ] Encryption of files and directories on disk to protect sensitive data
    - [ ] Examples: BitLocker for Windows, FileVault for macOS, dm-crypt for Linux
    - [ ] Ensures confidentiality and data security even if physical storage is compromised

  - [ ] **HTTPS (Secure Web Communication)**
    - [ ] Securing web communication through the use of SSL/TLS encryption
    - [ ] Protects data transmission between browsers and web servers
    - [ ] Ensures confidentiality, data integrity, and authentication of websites

  - [ ] **Email Encryption**
    - [ ] Encryption of email messages to prevent unauthorized access
    - [ ] Ensures the privacy of email communication
    - [ ] PGP (Pretty Good Privacy) and S/MIME are commonly used email encryption methods

  - [ ] **Digital Signatures**
    - [ ] Signing electronic documents to verify their authenticity and integrity
    - [ ] Used in legal contracts, software distribution, and email communication
    - [ ] Combines hashing and asymmetric encryption to create a unique signature

  - [ ] **Virtual Private Networks (VPNs)**
    - [ ] Encrypting network traffic over public networks to ensure privacy
    - [ ] Allows secure remote access to corporate networks
    - [ ] Uses tunneling protocols like IPSec and OpenVPN

  - [ ] **Secure Messaging Apps**
    - [ ] End-to-end encryption in messaging apps like WhatsApp and Signal
    - [ ] Protects the privacy of text messages, voice calls, and media sharing
    - [ ] Ensures only the intended recipient can decrypt and read the messages

  - [ ] **Blockchain and Cryptocurrencies**
    - [ ] Use of cryptographic principles for securing transactions and wallets
    - [ ] Bitcoin, Ethereum, and other cryptocurrencies rely on cryptographic algorithms
    - [ ] Ensures the immutability and security of transaction records

  - [ ] **Password Storage**
    - [ ] Storing passwords securely using cryptographic hashing algorithms
    - [ ] Protects user passwords in databases from being easily compromised
    - [ ] Salting and key stretching are common techniques

  - [ ] **Secure Shell (SSH)**
    - [ ] Authentication and secure remote login to servers over untrusted networks
    - [ ] Uses cryptographic keys for authentication and encryption
    - [ ] Replaces less secure protocols like Telnet

  - [ ] **Data-at-Rest Encryption (DARE)**
    - [ ] Encryption of data stored on various devices, including smartphones and laptops
    - [ ] Ensures data remains confidential even if the device is lost or stolen
    - [ ] Often combined with device authentication (e.g., biometrics)

  - [ ] **IoT (Internet of Things) Security**
    - [ ] Cryptography to secure communication between IoT devices and servers
    - [ ] Protects against unauthorized access and data breaches
    - [ ] Ensures the integrity of data collected from IoT sensors
