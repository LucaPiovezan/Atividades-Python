from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
<html lang="pt-BR">

<head>
  <link rel="icon" type="image/png" href="arvore.png">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Luca Piovezan — Portfólio</title>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Crimson+Pro:ital,wght@0,300;0,400;1,300;1,400&family=DM+Mono:wght@300;400&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

    :root {
      --ink: #0a0a0b;
      --paper: #f0ede8;
      --cream: #e8e3dc;
      --mist: #c8c3bc;
      --ghost: #8a857e;
      --accent: #e8501a;
      --accent2: #e8501a;
      --gold: #c8a44a;
      --glass-bg: rgba(240, 237, 232, 0.55);
      --glass-border: rgba(200, 195, 188, 0.35);
      --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
      --ease-in-out: cubic-bezier(0.85, 0, 0.15, 1);
    }

    html { scroll-behavior: smooth; font-size: 16px; }

    body {
      background: var(--paper);
      color: var(--ink);
      font-family: 'Crimson Pro', Georgia, serif;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.055'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 9998;
      mix-blend-mode: multiply;
    }

    #progress {
      position: fixed;
      top: 0; left: 0;
      height: 2px;
      background: var(--accent);
      z-index: 10001;
      width: 0%;
      transition: width 0.05s linear;
    }

    .hdr {
      position: fixed;
      top: 0; left: 0; right: 0;
      padding: 24px 56px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 300;
    }

    .hdr .logo {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 1.3rem;
      letter-spacing: 0.35em;
      color: var(--ink);
    }

    .hdr nav {
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      align-items: center;
    }

    .hdr nav a {
      font-family: 'DM Mono', monospace;
      font-size: 0.65rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      text-decoration: none;
      color: var(--ghost);
      margin-left: 40px;
      transition: color 0.3s;
      position: relative;
    }

    .hdr nav a:hover { color: var(--ink); }

    .hdr nav a::after {
      content: '';
      position: absolute;
      bottom: -3px; left: 0;
      width: 0; height: 1px;
      background: var(--accent);
      transition: width 0.4s var(--ease-out);
    }

    .hdr nav a:hover::after { width: 100%; }

    .scroll-stage {
      height: 500vh;
      position: relative;
    }

    .sticky-viewport {
      position: sticky;
      top: 0;
      height: 100vh;
      overflow: hidden;
      perspective: 1800px;
      perspective-origin: 50% 45%;
      background: var(--paper);
    }

    .sticky-viewport::before {
      content: '';
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 60% 60% at 20% 50%, rgba(232, 80, 26, 0.06) 0%, transparent 70%),
        radial-gradient(ellipse 60% 60% at 80% 50%, rgba(232, 80, 26, 0.05) 0%, transparent 70%);
      pointer-events: none;
      z-index: 0;
    }

    #floatCard {
      position: absolute;
      width: clamp(260px, 28vw, 360px);
      aspect-ratio: 2 / 3;
      transform-style: preserve-3d;
      will-change: transform;
      top: 0; left: 0;
      z-index: 20;
    }

    .card-face {
      position: absolute;
      inset: 0;
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
      border-radius: 16px;
      overflow: hidden;
    }

    .card-front {
      background: var(--ink);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 0;
      overflow: hidden;
    }

    .card-front .card-label {
      padding: 28px 32px 32px;
      background: linear-gradient(to top, rgba(0,0,0,0.75) 0%, transparent 100%);
      position: relative;
      z-index: 2;
    }

    .card-label .cl-name {
      font-family: 'DM Mono', monospace;
      font-size: 0.6rem;
      letter-spacing: 0.3em;
      color: rgba(240,237,232,0.6);
      text-transform: uppercase;
      margin-bottom: 8px;
    }

    .card-label .cl-role {
      font-family: 'Crimson Pro', serif;
      font-size: 1.4rem;
      font-weight: 300;
      font-style: italic;
      color: rgba(240,237,232,0.95);
      line-height: 1.3;
    }

    .card-back {
      transform: rotateY(180deg);
      background: var(--cream);
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 48px 36px;
      text-align: center;
      border: 1px solid var(--glass-border);
    }

    .card-back .cb-number {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 7rem;
      line-height: 0.8;
      color: var(--ink);
      opacity: 0.06;
      position: absolute;
      bottom: 20px; right: 24px;
      letter-spacing: -0.03em;
    }

    .card-back h3 {
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(2.5rem, 4vw, 3.5rem);
      line-height: 0.9;
      letter-spacing: 0.02em;
      color: var(--ink);
      margin-bottom: 24px;
    }

    .card-back h3 em {
      display: block;
      font-family: 'Crimson Pro', serif;
      font-style: italic;
      font-weight: 300;
      color: var(--accent);
    }

    .card-back p {
      font-family: 'DM Mono', monospace;
      font-size: 0.6rem;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--ghost);
    }

    .card-glow {
      position: absolute;
      left: 10%; right: 10%; bottom: -50px;
      height: 50px;
      background: radial-gradient(ellipse at center, rgba(10,10,11,0.25) 0%, transparent 70%);
      filter: blur(8px);
      pointer-events: none;
      z-index: -1;
      will-change: transform, opacity;
    }

    .txt-panel {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: clamp(280px, 38vw, 440px);
      opacity: 0;
      pointer-events: none;
      z-index: 60;
      padding: 40px 44px;
      background: var(--glass-bg);
      backdrop-filter: blur(24px) saturate(1.5);
      -webkit-backdrop-filter: blur(24px) saturate(1.5);
      border-radius: 4px;
      border: 1px solid var(--glass-border);
      box-shadow: 0 2px 0 rgba(255,255,255,0.6) inset, 0 40px 80px rgba(10,10,11,0.07);
    }

    .panel-eyebrow {
      font-family: 'DM Mono', monospace;
      font-size: 0.58rem;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: var(--ghost);
      margin-bottom: 20px;
    }

    .panel-eyebrow::before { content: '—  '; color: var(--accent); }

    .panel-h {
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(3.5rem, 5.5vw, 5.5rem);
      line-height: 0.88;
      letter-spacing: 0.01em;
      text-transform: uppercase;
      color: var(--ink);
      margin-bottom: 36px;
    }

    .panel-h span { display: block; color: var(--ink); }

    .panel-list { list-style: none; }

    .panel-list li {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      padding: 13px 0;
      border-top: 1px solid rgba(10,10,11,0.07);
      gap: 16px;
    }

    .panel-list li:last-child { border-bottom: 1px solid rgba(10,10,11,0.07); }

    .panel-list .pl-key {
      font-family: 'DM Mono', monospace;
      font-size: 0.58rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--ghost);
      flex-shrink: 0;
    }

    .panel-list .pl-val { font-size: 0.9rem; font-weight: 300; color: var(--ink); text-align: right; }

    .txt-panel::before {
      content: '';
      position: absolute;
      top: 0; right: 0;
      width: 40px; height: 40px;
      border-top: 1px solid var(--accent);
      border-right: 1px solid var(--accent);
      border-radius: 0 4px 0 0;
      opacity: 0.4;
    }

    .corner-label {
      position: absolute;
      bottom: 48px; right: 48px;
      font-family: 'DM Mono', monospace;
      font-size: 0.58rem;
      letter-spacing: 0.4em;
      text-transform: uppercase;
      color: var(--mist);
      writing-mode: vertical-rl;
      user-select: none;
    }

    #scroll-hint {
      position: absolute;
      bottom: 32px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
      z-index: 100;
      pointer-events: none;
      transition: opacity 0.6s ease;
    }

    #scroll-hint .sh-label {
      font-family: 'DM Mono', monospace;
      font-size: 0.55rem;
      letter-spacing: 0.35em;
      text-transform: uppercase;
      color: var(--ghost);
    }

    #scroll-hint .sh-track {
      width: 1px;
      height: 52px;
      background: rgba(138,133,126,0.2);
      border-radius: 2px;
      position: relative;
      overflow: hidden;
    }

    #scroll-hint .sh-fill {
      position: absolute;
      top: 0; left: 0;
      width: 100%;
      height: 40%;
      background: var(--accent);
      border-radius: 2px;
      animation: sh-drop 1.6s ease-in-out infinite;
    }

    @keyframes sh-drop {
      0%   { top: -40%; opacity: 1; }
      80%  { top: 110%; opacity: 0.6; }
      100% { top: 110%; opacity: 0; }
    }

    .dark-section {
      background: var(--ink);
      position: relative;
      overflow: hidden;
      padding: 140px 7% 100px;
    }

    .orb {
      position: absolute;
      border-radius: 50%;
      pointer-events: none;
      will-change: transform;
      animation: orb-float 18s ease-in-out infinite alternate;
    }

    .orb-1 { width: 700px; height: 700px; background: radial-gradient(circle, rgba(232,80,26,0.18) 0%, transparent 70%); top: -200px; right: -100px; filter: blur(80px); }
    .orb-2 { width: 500px; height: 500px; background: radial-gradient(circle, rgba(232,80,26,0.15) 0%, transparent 70%); bottom: 0; left: -100px; filter: blur(80px); animation-delay: -6s; }
    .orb-3 { width: 350px; height: 350px; background: radial-gradient(circle, rgba(200,164,74,0.12) 0%, transparent 70%); top: 40%; left: 45%; filter: blur(60px); animation-delay: -12s; }

    @keyframes orb-float {
      0%   { transform: translate(0,0) scale(1); }
      100% { transform: translate(-60px,-80px) scale(1.15); }
    }

    .section-tag {
      font-family: 'DM Mono', monospace;
      font-size: 0.6rem;
      letter-spacing: 0.4em;
      text-transform: uppercase;
      color: var(--ghost);
      margin-bottom: 28px;
      position: relative;
      z-index: 2;
    }

    .section-tag::before { content: '[ '; color: var(--accent); }
    .section-tag::after  { content: ' ]'; color: var(--accent); }

    .dark-heading {
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(5rem, 12vw, 13rem);
      line-height: 0.82;
      text-transform: uppercase;
      letter-spacing: -0.02em;
      color: var(--paper);
      margin-bottom: 100px;
      position: relative;
      z-index: 2;
    }

    .dark-heading em {
      display: block;
      font-family: 'Crimson Pro', serif;
      font-style: italic;
      font-weight: 300;
      color: transparent;
      -webkit-text-stroke: 1px rgba(240,237,232,0.3);
    }

    .skills-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1px;
      background: rgba(240,237,232,0.06);
      border: 1px solid rgba(240,237,232,0.06);
      border-radius: 4px;
      overflow: visible;
      position: relative;
      z-index: 2;
      margin-bottom: 1px;
      perspective: 1000px;
    }

    .skill-card {
      background: rgba(10,10,11,0.95);
      padding: 44px 36px;
      min-height: 240px;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      position: relative;
      overflow: hidden;
      transition: transform 0.12s ease, box-shadow 0.4s;
      will-change: transform;
    }

    .skill-card::before {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(600px circle at var(--mx,50%) var(--my,50%), rgba(240,237,232,0.04), transparent 50%);
      opacity: 0;
      transition: opacity 0.5s;
      z-index: 0;
    }

    .skill-card:hover::before { opacity: 1; }

    .skill-card::after {
      content: '';
      position: absolute;
      bottom: 0; left: 0; right: 0;
      height: 2px;
      background: linear-gradient(90deg, var(--accent), var(--accent2));
      transform: scaleX(0);
      transform-origin: left;
      transition: transform 0.5s var(--ease-out);
    }

    .skill-card:hover::after { transform: scaleX(1); }

    .skill-num {
      position: absolute;
      top: 24px; left: 28px;
      font-family: 'DM Mono', monospace;
      font-size: 0.58rem;
      letter-spacing: 0.25em;
      color: rgba(240,237,232,0.15);
      z-index: 1;
    }

    .skill-icon {
      font-size: 3.5rem;
      position: absolute;
      top: 50%; right: 28px;
      transform: translateY(-60%);
      opacity: 0.06;
      transition: opacity 0.4s, transform 0.5s var(--ease-out);
      z-index: 1;
      line-height: 1;
    }

    .skill-card:hover .skill-icon { opacity: 0.15; transform: translateY(-65%) scale(1.1); }

    .skill-name {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 2.2rem;
      letter-spacing: 0.02em;
      text-transform: uppercase;
      color: var(--paper);
      position: relative;
      z-index: 1;
      margin-bottom: 8px;
    }

    .skill-desc {
      font-size: 0.88rem;
      font-weight: 300;
      color: rgba(240,237,232,0.35);
      line-height: 1.65;
      position: relative;
      z-index: 1;
      max-width: 200px;
    }

    .marquee-wrap {
      overflow: hidden;
      border-top: 1px solid rgba(240,237,232,0.06);
      border-bottom: 1px solid rgba(240,237,232,0.06);
      padding: 26px 0;
      margin: 100px 0;
      position: relative;
      z-index: 2;
    }

    .marquee-track {
      display: flex;
      white-space: nowrap;
      animation: marquee 22s linear infinite;
    }

    .marquee-track span {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 1.05rem;
      letter-spacing: 0.35em;
      text-transform: uppercase;
      color: rgba(240,237,232,0.12);
      padding-right: 56px;
    }

    .marquee-track span.hi {
      color: var(--accent);
      opacity: 1;
      font-family: 'Crimson Pro', serif;
      font-style: italic;
      font-size: 1.1rem;
      letter-spacing: 0.05em;
    }

    @keyframes marquee {
      from { transform: translateX(0); }
      to   { transform: translateX(-50%); }
    }

    .projects-row {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1px;
      background: rgba(240,237,232,0.06);
      border: 1px solid rgba(240,237,232,0.06);
      border-radius: 4px;
      overflow: visible;
      position: relative;
      z-index: 2;
      perspective: 1000px;
    }

    .project-card {
      background: rgba(10,10,11,0.95);
      padding: 44px 36px 54px;
      position: relative;
      overflow: hidden;
      transition: transform 0.12s ease, box-shadow 0.4s;
      will-change: transform;
      cursor: pointer;
    }

    .project-card:hover { background: rgba(15,15,16,0.98); }

    .project-card::before {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(600px circle at var(--mx,50%) var(--my,50%), rgba(240,237,232,0.04), transparent 50%);
      opacity: 0;
      transition: opacity 0.5s;
      pointer-events: none;
    }

    .project-card:hover::before { opacity: 1; }

    .proj-tag {
      font-family: 'DM Mono', monospace;
      font-size: 0.58rem;
      letter-spacing: 0.28em;
      text-transform: uppercase;
      margin-bottom: 28px;
      position: relative;
      z-index: 1;
    }

    .project-card:nth-child(1) .proj-tag { color: var(--accent); }
    .project-card:nth-child(2) .proj-tag { color: var(--gold); }
    .project-card:nth-child(3) .proj-tag { color: var(--accent2); }

    .proj-title {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 2.4rem;
      line-height: 0.9;
      text-transform: uppercase;
      color: var(--paper);
      margin-bottom: 20px;
      position: relative;
      z-index: 1;
    }

    .proj-desc {
      font-size: 0.92rem;
      font-weight: 300;
      color: rgba(240,237,232,0.4);
      line-height: 1.7;
      position: relative;
      z-index: 1;
    }

    .proj-arrow {
      position: absolute;
      bottom: 32px; right: 32px;
      width: 40px; height: 40px;
      border: 1px solid rgba(240,237,232,0.1);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--paper);
      font-size: 1rem;
      z-index: 1;
      transition: background 0.3s, border-color 0.3s, transform 0.4s var(--ease-out);
    }

    .project-card:hover .proj-arrow { background: var(--accent); border-color: var(--accent); transform: translate(4px,-4px); }

    .contact-section {
      background: var(--paper);
      padding: 140px 7% 120px;
      display: grid;
      grid-template-columns: 1fr 1.1fr;
      gap: 80px;
      align-items: start;
      position: relative;
    }

    .contact-section::before {
      content: '';
      position: absolute;
      top: 0; left: 7%; right: 7%;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(10,10,11,0.12), transparent);
    }

    .contact-left { padding-top: 8px; }

    .contact-label {
      font-family: 'DM Mono', monospace;
      font-size: 0.6rem;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: var(--ghost);
      margin-bottom: 32px;
    }

    .contact-heading {
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(3.5rem, 8vw, 9rem);
      line-height: 0.85;
      text-transform: uppercase;
      letter-spacing: -0.02em;
      color: var(--ink);
      margin-bottom: 40px;
    }

    .contact-heading em {
      display: block;
      font-family: 'Crimson Pro', serif;
      font-style: italic;
      font-weight: 300;
      color: var(--accent);
    }

    .contact-subtext {
      font-size: 1.1rem;
      font-weight: 300;
      color: var(--ghost);
      line-height: 1.7;
      max-width: 340px;
    }

    .contact-links {
      display: flex;
      flex-direction: column;
      padding-top: 60px;
    }

    .contact-link {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 22px 0;
      border-bottom: 1px solid rgba(10,10,11,0.09);
      text-decoration: none;
      color: var(--ink);
      transition: color 0.3s, padding-left 0.4s var(--ease-out);
      position: relative;
      overflow: hidden;
    }

    .contact-link:first-child { border-top: 1px solid rgba(10,10,11,0.09); }

    .contact-link::before {
      content: '';
      position: absolute;
      left: 0; top: 0; bottom: 0;
      width: 0;
      background: rgba(232,80,26,0.05);
      transition: width 0.4s var(--ease-out);
    }

    .contact-link:hover { color: var(--accent); padding-left: 16px; }
    .contact-link:hover::before { width: 100%; }

    .link-name {
      font-family: 'DM Mono', monospace;
      font-size: 0.72rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
    }

    .link-arrow {
      width: 32px; height: 32px;
      border: 1px solid currentColor;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.9rem;
      opacity: 0.4;
      transition: opacity 0.3s, transform 0.4s var(--ease-out);
    }

    .contact-link:hover .link-arrow { opacity: 1; transform: translate(4px,-4px) rotate(45deg); }

    .footer {
      background: var(--ink);
      padding: 36px 7%;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .footer-copy {
      font-family: 'DM Mono', monospace;
      font-size: 0.58rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: rgba(240,237,232,0.2);
    }

    .footer-sig {
      font-family: 'Crimson Pro', serif;
      font-style: italic;
      font-size: 1.2rem;
      color: rgba(240,237,232,0.15);
    }

    .rv {
      opacity: 0;
      transform: translateY(36px);
      transition: opacity 0.9s var(--ease-out), transform 0.9s var(--ease-out);
    }

    .rv.in { opacity: 1; transform: translateY(0); }

    .bg-typo {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(10rem, 24vw, 35rem);
      line-height: 0.8;
      color: transparent;
      -webkit-text-stroke: 1px rgba(10,10,11,0.04);
      z-index: 1;
      pointer-events: none;
      text-align: center;
      letter-spacing: -0.02em;
      user-select: none;
      will-change: transform;
    }

    .desktop-hero {
      position: absolute;
      top: 50%;
      left: 52%;
      transform: translateY(-50%);
      z-index: 10;
      pointer-events: none;
      will-change: opacity, transform;
    }

    .dh-tag {
      font-family: 'DM Mono', monospace;
      font-size: 0.65rem;
      letter-spacing: 0.4em;
      text-transform: uppercase;
      color: var(--ghost);
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .dh-tag::before { content: ''; width: 40px; height: 1px; background: var(--accent); }

    .dh-title {
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(6rem, 11vw, 12rem);
      line-height: 0.85;
      letter-spacing: -0.01em;
      color: var(--ink);
      margin-bottom: 25px;
    }
    .dh-title em {
      display: block;
      font-family: 'Crimson Pro', serif;
      font-style: italic;
      font-weight: 300;
      color: var(--accent);
      font-size: 0.8em;
      margin-top: 8px;
    }

    .dh-desc {
      font-family: 'Crimson Pro', serif;
      font-size: 1.3rem;
      font-weight: 300;
      color: var(--ghost);
      line-height: 1.5;
      max-width: 440px;
    }

    .finale-split {
      position: absolute;
      top: 50%; left: 0; right: 0;
      transform: translate3d(0, -50%, 0);
      pointer-events: none;
      z-index: 10;
      opacity: 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 5vw;
    }

    .fs-left { display: flex; flex-direction: column; }
    .fs-right { display: flex; flex-direction: column; align-items: flex-end; text-align: right; }

    .fs-eyebrow {
      font-family: 'DM Mono', monospace;
      font-size: 0.65rem;
      letter-spacing: 0.4em;
      text-transform: uppercase;
      color: var(--ghost);
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .fs-eyebrow::before { content: ''; width: 40px; height: 1px; background: var(--accent); opacity: 0.5; }

    .fs-title {
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(6.5rem, 11vw, 13rem);
      line-height: 0.8;
      letter-spacing: 0.02em;
      color: var(--ink);
    }

    .fs-right .fs-title {
      font-family: 'Crimson Pro', serif;
      font-style: italic;
      font-weight: 300;
      color: var(--accent);
      font-size: clamp(5.5rem, 9vw, 10rem);
      line-height: 0.9;
      letter-spacing: 0;
      text-transform: lowercase;
    }

    /* ═══════════════════════════════════
       MOBILE
    ═══════════════════════════════════ */
    @media (max-width: 768px) {

      /* Header transparente — sem fundo preto que corta o logo */
      .hdr {
        padding: 20px 22px;
        background: transparent;
        backdrop-filter: none;
        -webkit-backdrop-filter: none;
        border-bottom: none;
        box-shadow: none;
      }

      .hdr .logo {
        font-size: 1.05rem;
        letter-spacing: 0.22em;
        color: var(--ink);
      }

      /* Nav pill no BOTTOM — completamente separada do header */
      .hdr nav {
        position: fixed;
        bottom: 24px;
        left: 50%;
        top: auto;
        transform: translateX(-50%);
        background: rgba(10,10,11,0.88);
        backdrop-filter: blur(24px) saturate(1.6);
        -webkit-backdrop-filter: blur(24px) saturate(1.6);
        padding: 14px 28px;
        border-radius: 100px;
        border: 1px solid rgba(255,255,255,0.09);
        box-shadow: 0 8px 32px rgba(0,0,0,0.28), 0 1px 0 rgba(255,255,255,0.06) inset;
        width: auto;
        max-width: calc(100vw - 40px);
        white-space: nowrap;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
      }

      .hdr nav a {
        margin: 0;
        padding: 0 16px;
        font-size: 0.6rem;
        letter-spacing: 0.16em;
        color: rgba(240,237,232,0.58);
        transition: color 0.25s;
        flex-shrink: 0;
        position: relative;
      }

      .hdr nav a:hover,
      .hdr nav a:active { color: var(--accent); }
      .hdr nav a::after { display: none; }

      /* Divisor vertical fino entre links */
      .hdr nav a + a::before {
        content: '';
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 1px;
        height: 12px;
        background: rgba(255,255,255,0.15);
      }

      .scroll-stage {
        height: auto !important;
        min-height: 100vh;
        position: relative;
      }

      .sticky-viewport {
        position: relative !important;
        top: auto !important;
        height: auto !important;
        min-height: 100vh;
        overflow: visible;
        perspective: none;
        perspective-origin: unset;
        display: flex;
        flex-direction: column;
        align-items: stretch;
        justify-content: flex-start;
      }

      #floatCard { display: none; }
      .card-glow  { display: none; }

      #pnl1, #pnl2, #pnl3 { display: none !important; }
      #scroll-hint { display: none; }
      .corner-label { display: none; }
      .bg-typo { display: none; }
      .desktop-hero { display: none; }

      .mobile-hero {
        display: flex !important;
        flex-direction: column;
        min-height: 100vh;
        width: 100%;
        position: relative;
        top: 0; left: 0;
        padding: 80px 24px 100px;
        overflow: hidden;
      }

      .mh-top {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
      }

      .mh-tag {
        font-family: 'DM Mono', monospace;
        font-size: 0.58rem;
        letter-spacing: 0.35em;
        text-transform: uppercase;
        color: var(--ghost);
        margin-bottom: 18px;
        display: flex;
        align-items: center;
        gap: 10px;
      }

      .mh-tag::before {
        content: '';
        display: inline-block;
        width: 24px;
        height: 1px;
        background: var(--accent);
      }

      .mh-name {
        font-family: 'Bebas Neue', sans-serif;
        font-size: clamp(4.5rem, 22vw, 7rem);
        line-height: 0.84;
        letter-spacing: -0.01em;
        color: var(--ink);
        margin-bottom: 6px;
      }

      .mh-name em {
        font-family: 'Crimson Pro', serif;
        font-style: italic;
        font-weight: 300;
        color: var(--accent);
        font-size: 0.62em;
        display: block;
        letter-spacing: 0;
      }

      .mh-role {
        font-family: 'Crimson Pro', serif;
        font-size: 1.1rem;
        font-style: italic;
        font-weight: 300;
        color: var(--ghost);
        margin-top: 16px;
        margin-bottom: 32px;
        line-height: 1.5;
      }

      .mh-cards {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-bottom: 28px;
      }

      .mh-card {
        background: var(--cream);
        border: 1px solid rgba(10,10,11,0.07);
        border-radius: 12px;
        padding: 16px 18px;
        position: relative;
        overflow: hidden;
      }

      .mh-card::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 2px;
        background: var(--accent);
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.4s var(--ease-out);
      }

      .mh-card:active::after { transform: scaleX(1); }

      .mh-card-key {
        font-family: 'DM Mono', monospace;
        font-size: 0.5rem;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        color: var(--ghost);
        margin-bottom: 6px;
      }

      .mh-card-val {
        font-family: 'Crimson Pro', serif;
        font-size: 0.95rem;
        font-weight: 300;
        color: var(--ink);
        line-height: 1.3;
      }

      .mh-cta {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: var(--ink);
        color: var(--paper);
        text-decoration: none;
        font-family: 'DM Mono', monospace;
        font-size: 0.6rem;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        padding: 14px 22px;
        border-radius: 100px;
        transition: background 0.3s, transform 0.3s var(--ease-out);
        align-self: flex-start;
      }

      .mh-cta:active { background: var(--accent); transform: scale(0.97); }

      .mh-cta-arrow {
        width: 22px; height: 22px;
        border: 1px solid rgba(240,237,232,0.25);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75rem;
      }

      .mh-photo-wrapper {
        position: absolute;
        top: 72px; right: -10px;
        width: 130px;
        height: 170px;
        border-radius: 14px;
        overflow: hidden;
        box-shadow: -8px 12px 40px rgba(10,10,11,0.18);
        border: 1px solid rgba(10,10,11,0.08);
        z-index: 10;
        will-change: transform;
        transform-style: preserve-3d;
        transform: perspective(400px) rotateY(0deg) rotateZ(3deg);
        transition: box-shadow 0.3s ease;
      }

      .mh-photo-wrapper img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center top;
        display: block;
        border-radius: 14px;
      }

      .mh-photo-wrapper::after {
        content: '';
        position: absolute;
        inset: 0;
        border-radius: 14px;
        background: linear-gradient(135deg, rgba(255,255,255,0.18) 0%, rgba(255,255,255,0) 50%, rgba(0,0,0,0.08) 100%);
        pointer-events: none;
        z-index: 2;
        transition: opacity 0.3s;
      }

      .mh-ghost-num {
        position: absolute;
        bottom: 90px; right: 20px;
        font-family: 'Bebas Neue', sans-serif;
        font-size: 7rem;
        color: rgba(10,10,11,0.04);
        line-height: 1;
        pointer-events: none;
        letter-spacing: -0.04em;
        z-index: 0;
      }

      .mh-scroll-prompt {
        position: absolute;
        bottom: 90px;
        left: 24px;
        display: flex;
        align-items: center;
        gap: 10px;
      }

      .mh-scroll-prompt span {
        font-family: 'DM Mono', monospace;
        font-size: 0.5rem;
        letter-spacing: 0.3em;
        text-transform: uppercase;
        color: var(--mist);
      }

      .mh-scroll-dot {
        width: 5px; height: 5px;
        border-radius: 50%;
        background: var(--accent);
        animation: pulse-dot 2s ease-in-out infinite;
      }

      @keyframes pulse-dot {
        0%, 100% { opacity: 0.4; transform: scale(1); }
        50%       { opacity: 1;   transform: scale(1.6); }
      }

      .mh-tag   { animation: mh-in 0.8s var(--ease-out) 0.1s both; }
      .mh-name  { animation: mh-in 0.9s var(--ease-out) 0.2s both; }
      .mh-role  { animation: mh-in 0.8s var(--ease-out) 0.32s both; }
      .mh-cards { animation: mh-in 0.8s var(--ease-out) 0.44s both; }
      .mh-cta   { animation: mh-in 0.8s var(--ease-out) 0.56s both; }
      .mh-photo-wrapper { animation: photo-in 1s var(--ease-out) 0.15s both; }

      @keyframes mh-in {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
      }

      @keyframes photo-in {
        from { opacity: 0; transform: perspective(400px) rotateY(-30deg) rotateZ(3deg) translateX(30px); }
        to   { opacity: 1; transform: perspective(400px) rotateY(0deg) rotateZ(3deg) translateX(0); }
      }

      .dark-section { padding: 64px 20px 56px; }

      .dark-heading {
        font-size: clamp(2.2rem, 13vw, 4rem);
        margin-bottom: 40px;
        line-height: 0.86;
        word-wrap: break-word;
        hyphens: auto;
      }

      .skills-grid {
        grid-template-columns: 1fr;
        gap: 12px;
        background: transparent;
        border: none;
      }

      .skill-card {
        border-radius: 14px;
        min-height: 120px;
        padding: 24px 20px 20px;
        border: 1px solid rgba(240,237,232,0.07);
      }

      .skill-num { top: 16px; left: 20px; font-size: 0.52rem; letter-spacing: 0.2em; color: rgba(240,237,232,0.12); }
      .skill-icon { font-size: 2.8rem; top: 50%; right: 20px; transform: translateY(-55%); opacity: 0.07; }
      .skill-name { font-size: 1.45rem; margin-bottom: 4px; margin-top: 22px; }
      .skill-desc { font-size: 0.72rem; max-width: 100%; color: rgba(240,237,232,0.28); line-height: 1.5; }

      .marquee-wrap { margin: 36px 0; padding: 18px 0; }
      .marquee-track span { font-size: 0.78rem; padding-right: 28px; letter-spacing: 0.22em; }
      .marquee-track span.hi { font-size: 0.85rem; }

      .projects-row { grid-template-columns: 1fr; gap: 10px; background: transparent; border: none; }

      .project-card {
        border-radius: 14px;
        padding: 28px 24px 64px;
        border: 1px solid rgba(240,237,232,0.07);
      }

      .proj-tag { font-size: 0.54rem; letter-spacing: 0.22em; margin-bottom: 16px; }
      .proj-title { font-size: 2.4rem; line-height: 0.88; }
      .proj-desc { font-size: 0.88rem; color: rgba(240,237,232,0.38); }
      .proj-arrow { bottom: 24px; right: 24px; width: 36px; height: 36px; font-size: 0.9rem; }

      .contact-section {
        grid-template-columns: 1fr;
        padding: 64px 20px 110px;
        gap: 24px;
      }

      .contact-section::before { left: 20px; right: 20px; }
      .contact-heading { font-size: clamp(3.5rem, 20vw, 5.5rem); margin-bottom: 16px; }
      .contact-subtext { font-size: 1rem; max-width: 100%; }
      .contact-label { margin-bottom: 20px; }
      .contact-left { padding-top: 0; }
      .contact-links { padding-top: 0; }
      .contact-link { padding: 18px 0; }
      .link-name { font-size: 0.6rem; letter-spacing: 0.14em; }
      .link-arrow { width: 28px; height: 28px; font-size: 0.8rem; }

      .footer {
        flex-direction: column;
        gap: 10px;
        padding: 28px 20px 100px;
        text-align: center;
      }
    }

    .mobile-hero { display: none; }
  </style>
</head>

<body>
  <div id="progress"></div>

  <header class="hdr">
    <div class="logo">Luca Piovezan</div>
    <nav>
      <a href="#stage">Exposição</a>
      <a href="#trabalho">Work</a>
      <a href="#contato">Contato</a>
    </nav>
  </header>

  <div class="scroll-stage" id="stage">
    <div class="sticky-viewport" id="viewport">

      <div class="bg-typo" id="bg-typo">CODE<br>DESIGN</div>

      <div class="desktop-hero" id="desktop-hero">
        <div class="dh-tag">Portfólio 2026</div>
        <h1 class="dh-title">Luca<br><em>Piovezan</em></h1>
        <p class="dh-desc">Desenvolvedor Front-end & Designer focado em criar experiências digitais imersivas.</p>
      </div>

      <div class="mobile-hero">
        <div class="mh-photo-wrapper" id="mh-photo">
          <img src="img.png" alt="Luca Piovezan">
        </div>
        <div class="mh-ghost-num"></div>

        <div class="mh-top">
          <div class="mh-tag">Front-end &amp; Design</div>
          <div class="mh-name">
            Luca<br>
            <em>Piovezan</em>
          </div>
          <div class="mh-role">Desenvolvedor de interfaces<br>imersivas e experiências digitais.</div>

          <div class="mh-cards">
            <div class="mh-card">
              <div class="mh-card-key">Stack</div>
              <div class="mh-card-val">HTML · CSS · JS</div>
            </div>
            <div class="mh-card">
              <div class="mh-card-key">Design</div>
              <div class="mh-card-val">Figma · Motion</div>
            </div>
            <div class="mh-card">
              <div class="mh-card-key">Formação</div>
              <div class="mh-card-val">Técnico em Info.</div>
            </div>
            <div class="mh-card">
              <div class="mh-card-key">Inglês</div>
              <div class="mh-card-val">B2 Intermediário</div>
            </div>
          </div>

          <a href="#trabalho" class="mh-cta">
            Ver Projetos
            <span class="mh-cta-arrow">↓</span>
          </a>
        </div>

        <div class="mh-scroll-prompt">
          <div class="mh-scroll-dot"></div>
          <span>Role para explorar</span>
        </div>
      </div>

      <div id="floatCard">
        <div class="card-face card-front">
          <img src="img.png" alt="Luca Piovezan"
            style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top;display:block;border-radius:16px;">
          <div class="card-label" style="position:relative;z-index:2;">
            <div class="cl-name">Front-end & Design</div>
            <div class="cl-role">Luca<br>Piovezan</div>
          </div>
        </div>
        <div class="card-face card-back">
          <h3>Design<br><em>Digital</em></h3>
          <p>HTML · CSS · JavaScript</p>
        </div>
        <div class="card-glow"></div>
      </div>

      <div class="txt-panel" id="pnl1" style="right:6%;left:auto;">
        <div class="panel-eyebrow">O que eu faço</div>
        <div class="panel-h">Desenvolver<br><span>Interfaces</span></div>
        <ul class="panel-list">
          <li><span class="pl-key">Foco</span><span class="pl-val">Experiências Imersivas</span></li>
          <li><span class="pl-key">Stack</span><span class="pl-val">HTML · CSS · JS</span></li>
          <li><span class="pl-key">Design</span><span class="pl-val">Figma & Animações</span></li>
        </ul>
      </div>

      <div class="txt-panel" id="pnl2" style="left:6%;right:auto;">
        <div class="panel-eyebrow">Minha história</div>
        <div class="panel-h">Código<br><span>&amp; Arte</span></div>
        <ul class="panel-list">
          <li><span class="pl-key">Formação</span><span class="pl-val">Técnico em Informática</span></li>
          <li><span class="pl-key">Escola</span><span class="pl-val">Colégio Cotemig</span></li>
          <li><span class="pl-key">Inglês</span><span class="pl-val">Intermediário B2</span></li>
        </ul>
      </div>

      <div id="pnl3" class="finale-split">
        <div class="fs-left">
          <div class="fs-eyebrow">Buscando Estágio</div>
          <div class="fs-title">VOU<br>ALÉM</div>
        </div>
        <div class="fs-right">
          <div class="fs-title">do<br>comum</div>
        </div>
      </div>

      <div id="scroll-hint">
        <span class="sh-label">Role</span>
        <div class="sh-track"><div class="sh-fill"></div></div>
      </div>

      <div class="corner-label">Luca · 2026 · Portfolio</div>
    </div>
  </div>

  <section class="dark-section" id="trabalho">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>

    <div class="section-tag rv">O que eu faço</div>
    <h2 class="dark-heading rv" style="transition-delay:.08s">Habilidades<br><em>Materializadas</em></h2>

    <div class="skills-grid rv" style="transition-delay:.16s">
      <div class="skill-card"><span class="skill-num">01</span><div class="skill-icon">◈</div><div class="skill-name">HTML & CSS</div><div class="skill-desc">Interfaces responsivas, semânticas e elegantes.</div></div>
      <div class="skill-card"><div class="skill-num">02</div><div class="skill-icon">⬡</div><div class="skill-name">JavaScript</div><div class="skill-desc">Lógica, interatividade e animações fluidas.</div></div>
      <div class="skill-card"><div class="skill-num">03</div><div class="skill-icon">◉</div><div class="skill-name">Python</div><div class="skill-desc">Lógica de programação e automação de tarefas.</div></div>
      <div class="skill-card"><div class="skill-num">04</div><div class="skill-icon">⬟</div><div class="skill-name">Figma</div><div class="skill-desc">Design de interfaces modernas e protótipos interativos.</div></div>
      <div class="skill-card"><div class="skill-num">05</div><div class="skill-icon">◐</div><div class="skill-name">UX Design</div><div class="skill-desc">Organização visual e foco na experiência do usuário.</div></div>
      <div class="skill-card"><div class="skill-num">06</div><div class="skill-icon">◇</div><div class="skill-name">Motion</div><div class="skill-desc">Animações e protótipos que comunicam com emoção.</div></div>
    </div>

    <div class="marquee-wrap rv" style="transition-delay:.24s">
      <div class="marquee-track">
        <span>HTML & CSS</span><span class="hi"> · código · </span>
        <span>JavaScript</span><span class="hi"> · lógica · </span>
        <span>Figma</span><span class="hi"> · design · </span>
        <span>Python</span><span class="hi"> · automação · </span>
        <span>HTML & CSS</span><span class="hi"> · código · </span>
        <span>JavaScript</span><span class="hi"> · lógica · </span>
        <span>Figma</span><span class="hi"> · design · </span>
        <span>Python</span><span class="hi"> · automação · </span>
      </div>
    </div>

    <div class="section-tag rv" style="transition-delay:.08s">Cases Selecionados</div>
    <div class="projects-row rv" style="transition-delay:.16s">
      <div class="project-card" onclick="window.open('https://lucapiovezan.github.io/Smart-flowers/','_blank')">
        <div class="proj-tag">Animação Parallax</div>
        <div class="proj-title">Smart<br>Flowers</div>
        <div class="proj-desc">E-commerce de flores com animações parallax imersivas.</div>
        <div class="proj-arrow">↗</div>
      </div>
      <div class="project-card" onclick="window.open('https://lucapiovezan.github.io/HEROES-VILLAINS/','_blank')">
        <div class="proj-tag">Projeto Imersivo · Three.js</div>
        <div class="proj-title">Heroes &<br>Villains</div>
        <div class="proj-desc">Experiência imersiva com WebGL e Three.js.</div>
        <div class="proj-arrow">↗</div>
      </div>
      <div class="project-card" onclick="window.open('https://lucapiovezan.github.io/valenza/','_blank')">
        <div class="proj-tag">E-commerce Automotivo</div>
        <div class="proj-title">Valenza<br>Garde</div>
        <div class="proj-desc">Plataforma automotiva com design premium e refinado.</div>
        <div class="proj-arrow">↗</div>
      </div>
    </div>
  </section>

  <section class="contact-section" id="contato">
    <div class="contact-left rv">
      <div class="contact-label">Vamos trabalhar juntos</div>
      <h2 class="contact-heading">Start<br><em>Here</em></h2>
      <p class="contact-subtext">Aberto a oportunidades de estágio e projetos desafiadores em desenvolvimento web e design de interfaces.</p>
    </div>
    <div class="rv" style="transition-delay:.1s">
      <div class="contact-links">
        <a href="mailto:lucapiovezan4@gmail.com" class="contact-link" target="_blank">
          <span class="link-name">lucapiovezan4@gmail.com</span>
          <span class="link-arrow">↗</span>
        </a>
        <a href="https://www.linkedin.com/in/luca-piovezan-6967aa3b4/" class="contact-link" target="_blank">
          <span class="link-name">LinkedIn</span>
          <span class="link-arrow">↗</span>
        </a>
        <a href="https://github.com/LucaPiovezan" class="contact-link" target="_blank">
          <span class="link-name">GitHub</span>
          <span class="link-arrow">↗</span>
        </a>
      </div>
    </div>
  </section>

  <footer class="footer">
    <span class="footer-copy">© 2026 Luca Piovezan — Todos os direitos reservados</span>
    <span class="footer-sig">LP</span>
  </footer>

  <script>
    const lerp = (a, b, t) => a + (b - a) * t;
    const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));
    const norm = (v, a, b) => clamp((v - a) / (b - a), 0, 1);
    const easeOutQuart = t => 1 - Math.pow(1 - t, 4);
    const easeInOutCubic = t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;

    const isMobile = () => window.innerWidth <= 768;

    const prog = document.getElementById('progress');
    window.addEventListener('scroll', () => {
      const h = document.documentElement;
      prog.style.width = (h.scrollTop / (h.scrollHeight - h.clientHeight) * 100) + '%';
    }, { passive: true });

    const scrollHint = document.getElementById('scroll-hint');
    window.addEventListener('scroll', () => {
      if (isMobile()) return;
      const p = window.scrollY / (document.documentElement.scrollHeight - innerHeight);
      scrollHint.style.opacity = p < 0.05 ? '1' : '0';
    }, { passive: true });

    const card = document.getElementById('floatCard');
    const stage = document.getElementById('stage');
    let CW = 0, CH = 0;

    function updateCardDims() {
      if (isMobile()) return;
      const r = card.getBoundingClientRect();
      CW = r.width; CH = r.height;
    }
    window.addEventListener('resize', updateCardDims);
    updateCardDims();

    let cX = 0, cY = 0, cRX = 0, cRY = 0, cS = 1;

    function getScrollProgress() {
      const r = stage.getBoundingClientRect();
      return clamp(-r.top / (stage.offsetHeight - innerHeight), 0, 1);
    }

    function getCardTargets(p) {
      const W = innerWidth, H = innerHeight;
      const safeTop = 90, safeBot = 40, padH = W * 0.12;
      const cardW = CW, cardH = CH;
      const availH = H - safeTop - safeBot - cardH;
      const cy = safeTop + Math.max(0, availH / 2);
      const lx = padH;
      const rx_ = Math.min(W - padH - cardW, W - cardW - padH);
      const cx = (W - cardW) / 2;
      const arcUp = Math.min(80, availH * 0.4);

      let oX = cx, oY = cy, rY = 0, rX = 0, s = 1;

      if (p < 0.08) {
        const t = easeInOutCubic(norm(p, 0, 0.08));
        oX = lerp(lx - 80, lx, t); oY = lerp(cy + 60, cy, t);
        rY = lerp(-35, 0, t); rX = lerp(12, 0, t); s = lerp(0.5, 1, t);
      } else if (p < 0.22) {
        const t = norm(p, 0.08, 0.22);
        oX = lx; oY = cy + Math.sin(t * Math.PI * 2) * 7;
        rY = Math.sin(t * Math.PI * 2) * 2.5; rX = Math.sin(t * Math.PI) * 1.5;
      } else if (p < 0.48) {
        const t = easeInOutCubic(norm(p, 0.22, 0.48));
        oX = lerp(lx, rx_, t); oY = cy - Math.sin(t * Math.PI) * arcUp;
        rY = t * 180; rX = Math.sin(t * Math.PI) * -20; s = 1 + Math.sin(t * Math.PI) * 0.05;
      } else if (p < 0.65) {
        const t = norm(p, 0.48, 0.65);
        oX = rx_; oY = cy + Math.sin(t * Math.PI * 2) * 7;
        rY = 180 + Math.sin(t * Math.PI * 2) * 3; rX = Math.sin(t * Math.PI) * 1.5;
      } else if (p < 0.88) {
        const t = easeInOutCubic(norm(p, 0.65, 0.88));
        oX = lerp(rx_, cx, t); oY = cy - Math.sin(t * Math.PI) * arcUp;
        rY = 180 + t * 180; rX = Math.sin(t * Math.PI) * -16;
        s = lerp(1, 1.05, easeInOutCubic(t));
      } else {
        const t = easeOutQuart(norm(p, 0.88, 1));
        oX = cx; oY = cy; rY = 360; rX = 0; s = lerp(1.05, 1.08, t);
      }

      oX = clamp(oX, 0, W - cardW);
      oY = clamp(oY, safeTop, H - safeBot - cardH);
      return { oX, oY, rY, rX, s };
    }

    function updatePanels(p) {
      const dh = document.getElementById('desktop-hero');
      const bgt = document.getElementById('bg-typo');
      if (dh) {
        const dhOut = clamp(norm(p, 0, 0.08), 0, 1);
        dh.style.opacity = 1 - easeOutQuart(dhOut);
        dh.style.transform = `translateY(calc(-50% - ${dhOut * 60}px))`;
      }
      if (bgt) {
        bgt.style.transform = `translate(-50%, calc(-50% - ${p * innerHeight * 0.8}px))`;
      }

      const pnl1 = document.getElementById('pnl1');
      const pnl2 = document.getElementById('pnl2');
      const pnl3 = document.getElementById('pnl3');

      const a1 = Math.max(0, clamp(norm(p, 0.08, 0.13), 0, 1) - clamp(norm(p, 0.20, 0.26), 0, 1));
      pnl1.style.opacity = a1;
      pnl1.style.transform = `translateY(calc(-50% + ${lerp(24, 0, easeOutQuart(a1))}px))`;
      pnl1.style.pointerEvents = a1 > 0.01 ? 'auto' : 'none';

      const a2 = Math.max(0, clamp(norm(p, 0.48, 0.54), 0, 1) - clamp(norm(p, 0.63, 0.68), 0, 1));
      pnl2.style.opacity = a2;
      pnl2.style.transform = `translateY(calc(-50% + ${lerp(24, 0, easeOutQuart(a2))}px))`;
      pnl2.style.pointerEvents = a2 > 0.01 ? 'auto' : 'none';

      const a3 = easeInOutCubic(clamp(norm(p, 0.88, 0.96), 0, 1));
      pnl3.style.opacity = a3;
      pnl3.style.transform = `translate3d(0, calc(-50% + ${lerp(40, 0, a3)}px), 0)`;
      pnl3.style.pointerEvents = a3 > 0.01 ? 'auto' : 'none';
    }

    const SPRING = 0.10;
    const glow = document.querySelector('.card-glow');

    function renderCard() {
      if (isMobile()) { requestAnimationFrame(renderCard); return; }
      if (!CW) updateCardDims();
      const p = getScrollProgress();
      const t = getCardTargets(p);

      cX  = lerp(cX,  t.oX, SPRING);
      cY  = lerp(cY,  t.oY, SPRING);
      cRX = lerp(cRX, t.rX, SPRING);
      cRY = lerp(cRY, t.rY, SPRING);
      cS  = lerp(cS,  t.s,  SPRING);

      card.style.transform = `translate3d(${cX}px,${cY}px,0) rotateX(${cRX}deg) rotateY(${cRY}deg) scale(${cS})`;

      const distFromCenter = Math.abs(cY - (innerHeight - CH) / 2);
      glow.style.opacity = Math.max(0.08, 0.45 - distFromCenter / 500);
      glow.style.transform = `scaleX(${Math.max(0.7, 1 - distFromCenter / 400)}) scaleY(${Math.max(0.3, 1 - distFromCenter / 300)})`;

      updatePanels(p);
      requestAnimationFrame(renderCard);
    }
    requestAnimationFrame(renderCard);

    const revEls = document.querySelectorAll('.rv');
    function checkRevs() {
      revEls.forEach(el => {
        if (el.getBoundingClientRect().top < innerHeight * 0.88) el.classList.add('in');
      });
    }
    window.addEventListener('scroll', checkRevs, { passive: true });
    checkRevs();

    if (!isMobile()) {
      document.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        if (!rect.width) return;
        const dx = (e.clientX - (rect.left + rect.width / 2)) / (innerWidth / 2);
        const dy = (e.clientY - (rect.top + rect.height / 2)) / (innerHeight / 2);
        card.style.transform = `translate3d(${cX}px,${cY}px,0) rotateX(${cRX + dy * -4}deg) rotateY(${cRY + dx * 6}deg) scale(${cS})`;
      });
    }

    document.querySelectorAll('.skill-card, .project-card, .contact-link').forEach(c => {
      c.addEventListener('mousemove', e => {
        if (isMobile()) return;
        const r = c.getBoundingClientRect();
        const x = e.clientX - r.left;
        const y = e.clientY - r.top;
        const dx = (x - r.width / 2) / (r.width / 2);
        const dy = (y - r.height / 2) / (r.height / 2);
        c.style.setProperty('--mx', x + 'px');
        c.style.setProperty('--my', y + 'px');
        c.style.transform = `perspective(800px) rotateX(${dy * -8}deg) rotateY(${dx * 10}deg) translateY(-8px) scale(1.02)`;
      });
      c.addEventListener('mouseleave', () => {
        if (isMobile()) return;
        c.style.transform = '';
        c.style.transition = 'transform 0.6s cubic-bezier(0.16,1,0.3,1)';
        setTimeout(() => c.style.transition = '', 600);
      });
    });

    if (isMobile()) {
      document.querySelectorAll('.project-card').forEach(c => {
        c.addEventListener('touchstart', () => { c.style.opacity = '0.85'; c.style.transform = 'scale(0.985)'; }, { passive: true });
        c.addEventListener('touchend', () => { c.style.opacity = ''; c.style.transform = ''; }, { passive: true });
      });
    }

    (function () {
      const photoWrapper = document.getElementById('mh-photo');
      if (!photoWrapper) return;

      let currentRotY = 0, currentRotZ = 3, targetRotY = 0, targetRotZ = 3, rafId = null;

      function applyTransform() {
        photoWrapper.style.transform = `perspective(500px) rotateY(${currentRotY}deg) rotateZ(${currentRotZ}deg)`;
        const absY = Math.abs(((currentRotY % 360) + 360) % 360);
        const shadowIntensity = absY > 90 && absY < 270 ? 0.05 : 0.18;
        photoWrapper.style.boxShadow = `-8px 12px 40px rgba(10,10,11,${shadowIntensity})`;
      }

      function animateSpin() {
        currentRotY += (targetRotY - currentRotY) * 0.15;
        currentRotZ += (targetRotZ - currentRotZ) * 0.15;
        applyTransform();
        const stillY = Math.abs(targetRotY - currentRotY) > 0.1;
        const stillZ = Math.abs(targetRotZ - currentRotZ) > 0.05;
        if (stillY || stillZ) { rafId = requestAnimationFrame(animateSpin); } else { rafId = null; }
      }

      window.addEventListener('scroll', () => {
        if (!isMobile()) return;
        if (photoWrapper.style.animation !== 'none') photoWrapper.style.animation = 'none';
        const scrollY = window.scrollY;
        const maxScroll = 400;
        const progress = Math.max(0, Math.min(scrollY / maxScroll, 1));
        targetRotY = progress * 180;
        targetRotZ = 3 + Math.sin(scrollY * 0.015) * 4;
        if (!rafId) rafId = requestAnimationFrame(animateSpin);
      }, { passive: true });

      applyTransform();
    })();
  </script>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
