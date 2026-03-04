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
    IF TG_OP = 'INSERT' THEN
        NEW.created_at := now();
        NEW.updated_at := now();

        IF auth.uid() IS NOT NULL THEN
            NEW.created_by := auth.uid();
            NEW.updated_by := auth.uid();
        ELSE
            NEW.created_by := 'f1d8fd7b-6f77-4603-9443-f64dcf6d9fe4';
            NEW.updated_by := 'f1d8fd7b-6f77-4603-9443-f64dcf6d9fe4';
        END IF;

    ELSIF TG_OP = 'UPDATE' THEN
        -- Preserve creation metadata
        NEW.created_at := OLD.created_at;
        NEW.created_by := OLD.created_by;

        -- Always update modification metadata
        NEW.updated_at := now();

        IF auth.uid() IS NOT NULL THEN
            NEW.updated_by := auth.uid();
        ELSE
            NEW.updated_by := 'f1d8fd7b-6f77-4603-9443-f64dcf6d9fe4';
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;