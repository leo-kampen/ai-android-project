# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Development Commands

- **Build the app**
  ```
  ./gradlew assembleDebug
  ```
  Builds the debug APK for installation.

- **Run the app (debug)**
  Open Android Studio or use `adb install` on the generated APK:
  ```
  ./gradlew installDebug
  ```

- **Run unit tests**
  ```
  ./gradlew testDebugUnitTest
  ```
  Executes tests in `app/src/test/java`.

- **Run a single unit test**
  Specify the test task with `-Dtest.single`:
  ```
  ./gradlew testDebugUnitTest -Dtest.single=com.example.ai_proj_test1.ui.MainActivityTest
  ```

- **Run instrumented (UI) tests**
  ```
  ./gradlew connectedAndroidTest
  ```

- **Lint the code**
  ```
  ./gradlew lintDebug
  ```

- **Run Gradle wrapper with any task**
  Prefix any Gradle task with `./gradlew` to ensure the correct wrapper is used.

## High‑Level Architecture

The project is a standard Android application written in Kotlin using Jetpack Compose:

- `app/src/main/java/com/example/ai_proj_test1/`
  - `MainActivity.kt` – the single entry point, hosts a Compose UI.
  - `ui/theme/` – Compose theme definitions.
  - No business logic or networking layers are present; the app currently serves as a minimal template.

- Gradle build files:
  - `build.gradle.kts` at the root and in `app/` define plugin versions, SDK settings, and dependencies.
  - The wrapper (`gradlew`, `gradlew.bat`) is used for reproducible builds.

- Testing:
  - Unit tests live in `app/src/test/java`.
  - Instrumented tests are in `app/src/androidTest/java`.

- The repository contains a `codex.py` script, a small LangChain agent that can be run with:
  ```
  python codex.py "<instruction>"
  ```
  It is not part of the Android build but can be useful for quick LLM‑powered code analysis within the repo.

## Useful Files

- `app/build.gradle.kts` – app‑specific Gradle configuration.
- `app/src/main/java/com/example/ai_proj_test1/MainActivity.kt` – main Compose UI.
- `codex.py` – optional helper script for language‑model driven tasks.
