# --- Stage 1: Base ---
FROM node:20-alpine AS base
WORKDIR /app

# --- Stage 2: Dependencies ---
FROM base AS deps
COPY package*.json ./
RUN npm ci

# --- Stage 3: Build ---
FROM base AS builder
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

# --- Stage 4: Production Runner ---
FROM base AS runner
ENV NODE_ENV=production

# Security: Run as non-root user
RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 expressuser

# Copy only production node_modules and built JavaScript files
COPY package*.json ./
RUN npm ci --only=production

COPY --from=builder --chown=expressuser:nodejs /app/dist ./dist

USER expressuser

EXPOSE 3003
ENV PORT=3003
ENV HOSTNAME="0.0.0.0"

CMD ["node", "dist/server.js"]