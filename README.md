# 🧠 CogniPlan AI

### Adaptive Agentic Learning System

> **CogniPlan AI is an adaptive learning engine that continuously analyzes learner performance, identifies knowledge gaps, and dynamically adapts future study strategies.**

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![CogniPlan CI](https://github.com/sanchita25bai11100/CogniPlan-AI/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/sanchita25bai11100/CogniPlan-AI/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚀 Overview

Traditional study planners create schedules.

**CogniPlan learns from the learner.**

Instead of generating a static timetable, CogniPlan models learning as a continuous feedback loop:

```text
        ┌─────────────────────┐
        │   STUDENT STATE     │
        │                     │
        │ Mastery             │
        │ Confidence          │
        │ Retention Risk      │
        │ Performance         │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │   PLANNER AGENT     │
        │                     │
        │ Prioritize tasks    │
        └──────────┬──────────┘
                   │
                   ▼
             STUDY SESSION
                   │
                   ▼
        ┌─────────────────────┐
        │  EVALUATOR AGENT    │
        │                     │
        │ Accuracy            │
        │ Confidence          │
        │ Efficiency          │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │ ADAPTATION AGENT    │
        │                     │
        │ Revision            │
        │ Practice            │
        │ Spaced Repetition   │
        │ Advancement         │
        └──────────┬──────────┘
                   │
                   ▼
                 REPLAN
                   │
                   └───────────────► 🔄
