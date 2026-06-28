from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from datetime import datetime

from database import Base


# -----------------------------
# USER TABLE
# -----------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, nullable=False)

    email = Column(String, unique=True, nullable=False)

    hashed_password = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)


# -----------------------------
# FILES TABLE
# -----------------------------
class FileRecord(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    original_name = Column(String, nullable=False)

    stored_name = Column(String, unique=True, nullable=False)

    file_path = Column(String, nullable=False)

    file_type = Column(String)

    file_size = Column(Integer)

    uploaded_at = Column(DateTime, default=datetime.utcnow)

    is_deleted = Column(Boolean, default=False)

    folder_id = Column(
        Integer,
        ForeignKey("folders.id"),
        nullable=True,
        index=True
    )


# -----------------------------
# SHARED FILES TABLE
# -----------------------------
class SharedFile(Base):
    __tablename__ = "shared_files"

    id = Column(Integer, primary_key=True, index=True)

    file_id = Column(
        Integer,
        ForeignKey("files.id"),
        nullable=False,
        index=True
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    target_user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    shared_at = Column(DateTime, default=datetime.utcnow)


# -----------------------------
# SHARED FOLDERS TABLE
# -----------------------------
class SharedFolder(Base):
    __tablename__ = "shared_folders"

    id = Column(Integer, primary_key=True, index=True)

    folder_id = Column(
        Integer,
        ForeignKey("folders.id"),
        nullable=False,
        index=True
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    target_user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    shared_at = Column(DateTime, default=datetime.utcnow)


# -----------------------------
# FOLDERS TABLE
# -----------------------------
class FolderRecord(Base):
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    name = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    is_deleted = Column(Boolean, default=False)


# -----------------------------
# NOTIFICATIONS TABLE
# -----------------------------
class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    message = Column(String, nullable=False)

    is_read = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)


# -----------------------------
# ACTIVITY LOG TABLE
# -----------------------------
class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    file_id = Column(
        Integer,
        ForeignKey("files.id"),
        nullable=True
    )

    action = Column(String, nullable=False)

    description = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
 