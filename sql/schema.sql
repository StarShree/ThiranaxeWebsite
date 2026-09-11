-- =============================================================================
-- Google Cloud SQL (MySQL 8.0) Database Schema for Personal Portfolio
-- Target Host: 34.100.184.249
-- Database: Portfoliodb
-- =============================================================================

CREATE DATABASE IF NOT EXISTS `Portfoliodb`
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE `Portfoliodb`;

-- -----------------------------------------------------------------------------
-- Table: portfolio_profile
-- Stores primary biographical, contact, and overview information
-- -----------------------------------------------------------------------------
DROP TABLE IF EXISTS `portfolio_profile`;
CREATE TABLE `portfolio_profile` (
    `id` BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `full_name` VARCHAR(100) NOT NULL,
    `tagline` VARCHAR(200) NOT NULL,
    `bio` LONGTEXT NOT NULL,
    `about_details` LONGTEXT NOT NULL,
    `years_of_experience` INT UNSIGNED NOT NULL DEFAULT 0,
    `completed_projects_count` INT UNSIGNED NOT NULL DEFAULT 0,
    `happy_clients_count` INT UNSIGNED NOT NULL DEFAULT 0,
    `location` VARCHAR(100) NOT NULL,
    `email` VARCHAR(254) NOT NULL,
    `phone` VARCHAR(30) NOT NULL,
    `github_url` VARCHAR(200) NOT NULL,
    `linkedin_url` VARCHAR(200) NOT NULL,
    `twitter_url` VARCHAR(200) NOT NULL,
    `resume_url` VARCHAR(200) NOT NULL,
    `avatar_url` VARCHAR(200) NOT NULL,
    `is_active` TINYINT(1) NOT NULL DEFAULT 1,
    `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- Table: portfolio_skillcategory
-- Groups technical skills into domains (Frontend, Backend, Cloud, DB)
-- -----------------------------------------------------------------------------
DROP TABLE IF EXISTS `portfolio_skill`;
DROP TABLE IF EXISTS `portfolio_skillcategory`;
CREATE TABLE `portfolio_skillcategory` (
    `id` BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` VARCHAR(60) NOT NULL,
    `icon` VARCHAR(50) NOT NULL DEFAULT 'code',
    `order` INT UNSIGNED NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- Table: portfolio_skill
-- Individual skills with proficiency percentages and icons
-- -----------------------------------------------------------------------------
CREATE TABLE `portfolio_skill` (
    `id` BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `proficiency` INT UNSIGNED NOT NULL DEFAULT 80,
    `icon_class` VARCHAR(50) NOT NULL DEFAULT '',
    `is_featured` TINYINT(1) NOT NULL DEFAULT 0,
    `order` INT UNSIGNED NOT NULL DEFAULT 0,
    `category_id` BIGINT NOT NULL,
    CONSTRAINT `fk_skill_category` FOREIGN KEY (`category_id`)
        REFERENCES `portfolio_skillcategory` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- Table: portfolio_project
-- Showcase projects with live links, GitHub repos, tech stack, and summaries
-- -----------------------------------------------------------------------------
DROP TABLE IF EXISTS `portfolio_project`;
CREATE TABLE `portfolio_project` (
    `id` BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `title` VARCHAR(150) NOT NULL,
    `slug` VARCHAR(160) NOT NULL UNIQUE,
    `category` VARCHAR(30) NOT NULL,
    `short_description` VARCHAR(255) NOT NULL,
    `full_description` LONGTEXT NOT NULL,
    `tech_stack` VARCHAR(255) NOT NULL,
    `image_url` VARCHAR(200) NOT NULL,
    `live_demo_url` VARCHAR(200) NOT NULL,
    `github_url` VARCHAR(200) NOT NULL,
    `is_featured` TINYINT(1) NOT NULL DEFAULT 1,
    `order` INT UNSIGNED NOT NULL DEFAULT 0,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- Table: portfolio_experience
-- Professional work history and roles
-- -----------------------------------------------------------------------------
DROP TABLE IF EXISTS `portfolio_experience`;
CREATE TABLE `portfolio_experience` (
    `id` BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `role` VARCHAR(120) NOT NULL,
    `company` VARCHAR(120) NOT NULL,
    `location` VARCHAR(100) NOT NULL,
    `start_date` VARCHAR(50) NOT NULL,
    `end_date` VARCHAR(50) NOT NULL DEFAULT 'Present',
    `description` LONGTEXT NOT NULL,
    `technologies` VARCHAR(255) NOT NULL,
    `order` INT UNSIGNED NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- Table: portfolio_education
-- Educational background, degrees, and institutions
-- -----------------------------------------------------------------------------
DROP TABLE IF EXISTS `portfolio_education`;
CREATE TABLE `portfolio_education` (
    `id` BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `degree` VARCHAR(150) NOT NULL,
    `institution` VARCHAR(150) NOT NULL,
    `period` VARCHAR(50) NOT NULL,
    `grade_or_details` LONGTEXT NOT NULL,
    `order` INT UNSIGNED NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------------------------------
-- Table: portfolio_contactmessage
-- Contact form submissions received from visitors
-- -----------------------------------------------------------------------------
DROP TABLE IF EXISTS `portfolio_contactmessage`;
CREATE TABLE `portfolio_contactmessage` (
    `id` BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `email` VARCHAR(254) NOT NULL,
    `subject` VARCHAR(200) NOT NULL,
    `message` LONGTEXT NOT NULL,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `is_read` TINYINT(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Indexes for optimal querying
CREATE INDEX `idx_project_category` ON `portfolio_project` (`category`);
CREATE INDEX `idx_project_featured` ON `portfolio_project` (`is_featured`);
CREATE INDEX `idx_skill_category_id` ON `portfolio_skill` (`category_id`);
CREATE INDEX `idx_contact_created_at` ON `portfolio_contactmessage` (`created_at`);
