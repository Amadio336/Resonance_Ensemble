# Resonance - Esemble Learning experimental solution

[ 🇮🇹 Leggi in Italiano ](#-italiano) | [ 🇬🇧 Read in English ](#-english)

## 🇬🇧 English

## Overview
Welcome! This is an experimental project created to study and design a solution to one of the main issues encountered when applying computational analysis techniques to Ancient Greek: **semantic disambiguation** (more details below ⬇️). The proposed solution focuses on combining traditional Greek morphology recognition systems with advanced machine learning tools (the **ensemble learning technique**) to minimize errors in the form disambiguation process, while keeping both economic and computational costs virtually at zero.

### Problem Description

The automatic morphological recognition used by Resonance is based on the **Standard Morphology Service API** (https://sites.tufts.edu/perseusupdates/2012/11/01/morphology-service-beta/), known as **Morpheus**, which is provided by the Perseus Digital Library. Although it is an incredibly powerful tool—with a practically zero error rate—it has several non-negligible limitations when deployed in a production environment. 

The main limitation is that it parses and **returns the morphological analysis of words without taking their context into account**. This implies that whenever there is a case of homonymy (which I refer to as a conflict), the system is unable to return a unique analysis of the word. Instead, it returns all possibilities, which are often numerous and difficult to manage. 

Resonance has only partially overcome this issue by offering the user the ability to:

1. Manually resolve each conflict via a dedicated interface.
2. Import a custom JSON file containing pre-processed information for every single word.

While these solutions are useful, they both present specific drawbacks. In particular: solution 1 makes the application inefficient when working with long texts; solution 2 fully resolves this issue, but the process of creating these support files is time-consuming.

## Proposed Solution

By using **Machine Learning models specialized in Ancient Greek analysis**, I decided to employ a technique known as **Ensemble learning**. In this specific context, it is particularly advantageous because it leverages the strengths of the deployed technologies and, more importantly, deeply mitigates their limitations. 

In practice, I sought to implement a system that still relies on the Morpheus API for non-problematic words, since *the main strength of this technology is its flawless analysis accuracy*. For conflicts, Morpheus **delegates the task of disambiguating word homonymy to multiple models from the Odycy suite**. Initial tests show this is a very promising strategy because these models—which have a non-negligible potential for errors (hallucinations)—do not have to completely re-analyze the words and context from scratch. Rather, they simply choose from the options already provided by the Morpheus API. Furthermore, using multiple models allows the system to assign a confidence score to each proposal, enabling it to accept the highest-scoring one. 

A possible **criticism** of this solution is the high computational cost it requires. However, the fact that Resonance can accept custom-built JSON files eliminates this problem: one can simply leverage this approach to efficiently create these files in a reasonable amount of time, without the need to rent expensive servers to run the models in real-time within the application.

**Note**:
As of now, only a **prototype** of this system has been implemented. 
It currently relies on two models (ideally, an odd number of models should be used) and only addresses major conflicts. The tests conducted so far are few and run on short text samples, meaning they are still insufficient. However, the results emerging from these initial tests are truly promising. Additionally, future developments might include using models from different families.

## 🇮🇹 Italiano

## In breve
Benvenuti! Questo è un progetto sperimentale nato per studiare e progettare una soluzione a uno delle principali problematiche di quando si applicano tecniche di analisi computazionale al greco antico: **la disambiguazione semantica** (maggiori dettagli sotto  ⬇️ ). La soluzione studiata si concentra sul combinare sistemi di riconoscimento tradizionali della morfologia greca con strumenti di machine learning avanzati (**tecnica dell'ensemble learning**) per ridurre al minimo errori nel processo di disambiguizzazione delle form,e mantenendo il costo sia economico che di potenza di calcolo preossocché nullo.


### Descrizione del problema

Il riconoscimento morfologico automatico che Resonance sfrutta è basato sul sistema di **Standard Morphology Service API** (https://sites.tufts.edu/perseusupdates/2012/11/01/morphology-service-beta/)conosciuto come **Morpheus** ed è messo a disposizione dalla Perseus Digital Library. Nonostante sia uno strumento incredibilmente potente - ha una percentuale di errore praticamente nulla - esso presenta diverse limitazioni, purtroppo non trascurabili, nell’utilizzo in produzione di tale strumento. 

La principale limitazione è che esso analizza e **restituisce l’analisi morfologica delle parole non tenendo conto del loro contesto**. Questo implica che ogni volta che ci sia un caso di omonimia (che io chiamo conflitto), tale sistema non è in grado di restituire univocamente l’analisi della parola, bensì restituisce tutte le possibilità, che spesso sono molte e di difficile gestione. 

Resonance ha superato solo parzialmente questo problema offrendo all’utente la possibilità di:

1. risolvere manualmente ogni conflitto tramite l’interfaccia dedicata.
2. importare un file in formato json dedicato con già le informazioni di ogni singola parola.

Si tratta di soluzioni utili, ma che contestualmente presentano ognuna degli svantaggi, in particolare: la soluzione 1 rende poco efficiente l’uso dell’applicazione quando si lavora con testi lunghi; la soluzione 2 risolve questo problema pienamente, tuttavia il processo per creare questi file di supporto è lungo. 


## Proposta di soluzione

Attraverso l’utilizzo di modelli di **Machine Learning specializzati per l’analisi del greco antico**, ho pensato di utilizzare una tecnica nota come **Ensemble**, che in questo specifico è particolarmente profittevole perché sfrutta i punti di forza delle tecnologie impiegate e, ancor più importante, ne mitiga profondamente le limitazioni. 

 Nella pratica, ho cercato di implementare un sistema che si basa ancora sul Morpheus API per le parole che non presentano alcuna problematicità, infatti _il punto di forza di questa tecnologia è il fatto di essere ineccepibile nell’analisi_. Per i conflitti, Morpheus **delega il compito di disambiguare l’omonimia delle parole a molteplici modelli della suite Odycy**. Si tratta di una strategia che, dai primi test, riesce a dare risultati molto interessanti perché questi modelli, che hanno un potenziale di errore (allucinazioni) non trascurabile, non devono rianalizzare totalmente le parole e il contesto, ma devono scegliere tra le opzioni fornite da Morpheus Api. Inoltre il fatto di avere più modelli permette di dare un punteggio alle proposte di ciascuno, in modo da accogliere quella con punteggio più alto. 

Una **critica** possibile a tale soluzione è l’alto costo computazionale che richiede, tuttavia il fatto che Resonance abbia la possibilità di accettare file json costruiti ad hoc, elimina il problema: basta semplicemente sfruttare questa soluzione per creare efficacemente e in tempi ragionevoli questi file, senza dover affittare costosi server per far girare i modelli in tempo reale sull’applicazione. 

**Nota**:
Per ora, è stata implementata una **bozza** di tale sistema. 
Esso che chiede l’aiuto di due modelli (l’ideale sarebbe avere un numero di modelli dispari) sui soli conflitti maggiori e i test fatti sono ancora pochi e su porzioni di testo brevi, pertanto insufficienti. Tuttavia, da questi pochi test emergono risultati davvero promettenti. Inoltre si potrebbe pensare di usare modelli di famiglie diverse.    