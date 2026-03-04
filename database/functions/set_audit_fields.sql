-- Function: set_audit_fields
-- Type: Trigger Function
-- Purpose:
--   - Prevent changes to created_at and created_by
--   - Automatically update updated_at
--   - Set updated_by from auth.uid() when available
-- Usage:
--   BEFORE UPDATE trigger on tables with audit columns
-- Created: 2026-03-04

CREATE OR REPLACE FUNCTION set_audit_fields()
RETURNS TRIGGER AS $$
BEGIN
    NEW.created_at = OLD.created_at;
    NEW.created_by = OLD.created_by;

    NEW.updated_at = now();

    IF auth.uid() IS NOT NULL THEN
        NEW.updated_by = auth.uid();
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;